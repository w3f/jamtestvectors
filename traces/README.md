# Block Import Traces

Import full blocks starting from genesis, implementing the complete logic
required of a block importer that complies with the specifications outlined
in Graypaper Milestone 1 (M1).

## Schema

The schema is designed to be sufficiently generic to allow easy processing by
any implementation aiming to undergo conformance testing.

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./schema.asn) defined for these test cases.

## Gas Costs

The gas cost for a single instruction is set to **$1$**, unlike in GP where
it is set to $0$. This distinction is primarily intended to verify correct
tracking of gas consumption.

All host calls have a gas cost of **$10$**, with the following exceptions:
- **`transfer`**: Gas cost is set to **$10 + \omega_9$**, as specified in the GP.
- **`log`**: Gas cost is set to **0**, as defined in [JIP-1](https://hackmd.io/@polkadot/jip1).

## Vectors

- [Fallback](./fallback): fallback block authoring, no-safrole, no-work-reports
- [Safrole](./safrole): safrole block authoring, no-work-reports
- [Reports L0](./reports-l0): no-safrole, basic work reports (read/write/info/log)
- [Reports L1](./reports-l1): no-safrole, preimages provision (solicit/forget/info/log)

## Preimage Expunge Delay

The GP defines a constant `D`, representing the number of timeslots after which
an unreferenced preimage may be expunged.

In the `full` configuration, the GP mandates `D = 19,200`, which corresponds to
exactly 32 full epochs (`E = 600`). Applying the same logic to the `tiny`
configuration, where `E = 12`, would yield `D = 12 × 32 = 384` slots.

However, this value is too large for a constrained set of test vectors with very
few blocks. For testing purposes, we have therefore chosen to use **`D = 32`**
instead.

**The final value of `D` for the `tiny` testnet remains undecided**,
and should be documented in the community-maintained
[chain spec documentation](https://docs.jamcha.in/basics/chain-spec/tiny) once determined.

## Notes on SBRK 

For [Work Reports L0](./reports-l0), there are many uses of SBRK in 11 test
vectors that involve an `accumulate` invocation.
Teams should follow [Jan's sbrk advice](https://paritytech.github.io/matrix-archiver/archive/_21ddsEwXlCWnreEGuqXZ_3Apolkadot.io/index.html#$_RkIlMDNZrROw_6WDXpbllO2VSbjY1FNTIfDjVZhhdw)
to pass these 11 cases. Below is a sufficient Go implementation following this advice.

Note that the `sbrk` instruction is expected to be replaced with a host function
(see [here](https://paritytech.github.io/matrix-archiver/archive/_21ddsEwXlCWnreEGuqXZ_3Apolkadot.io/index.html#$JU2fAJu00hr9dA0Yta2nmFhErxNHT5f_hXn2PZyckjg))
so any implementation work here should be seen as **temporary**.

### Implementation in Go

```go
// ... valueA, registerIndexD of SBRK 
if valueA == 0 {
    // The guest is querying the current heap pointer
    vm.WriteRegister(registerIndexD, uint64(vm.Ram.current_heap_pointer))
    return
}

// Record current heap pointer to return
result = uint64(vm.Ram.current_heap_pointer)

next_page_boundary := P_func(vm.Ram.current_heap_pointer)
new_heap_pointer := uint64(vm.Ram.current_heap_pointer) + valueA

if new_heap_pointer > uint64(next_page_boundary) {
    final_boundary := P_func(uint32(new_heap_pointer))
    idx_start := next_page_boundary / Z_P
    idx_end := final_boundary / Z_P
    page_count := idx_end - idx_start

    vm.Ram.allocatePages(idx_start, page_count)
}

// Advance the heap
vm.Ram.current_heap_pointer = uint32(new_heap_pointer)
```

#### Memory model 

The above utilizes a RAM object to support all read and writes via
`WriteRAMBytes` and `ReadRAMBytes` methods, used in LOAD + STORE operations, and
many host functions (READ, WRITE, INFO, etc.)

```go
type RAM struct {
    stack_address        uint32
    stack_address_end    uint32
    rw_data_address      uint32
    rw_data_address_end  uint32
    ro_data_address      uint32
    ro_data_address_end  uint32
    current_heap_pointer uint32
    output_address       uint32
    output_end           uint32

    stack   []byte
    rw_data []byte
    ro_data []byte
    output  []byte
}

func NewRAM(o_size uint32, w_size uint32, p_s uint32) *RAM {
    // read-only
    ro_data_address := uint32(Z_Z)
    ro_data_address_end := ro_data_address + o_size

    // read-write
    rw_data_address := uint32(2 * Z_Z)
    rw_data_address_end := rw_data_address + Z_func(o_size)
    current_heap_pointer := rw_data_address_end + Z_P  // Note: extra Z_P is debatable

    // stack
    stack_address := uint32(0xFFFFFFFF) - 2*Z_Z - Z_I - p_s + 1
    stack_address_end := stack_address + p_s

    // output
    a_size := uint32(Z_Z + Z_I - 1)
    output_address := uint32(0xFFFFFFFF) - Z_Z - Z_I + 1
    output_end := uint32(0xFFFFFFFF)

    return &RAM{
        stack_address:        stack_address,
        stack_address_end:    stack_address_end,
        rw_data_address:      rw_data_address,
        rw_data_address_end:  rw_data_address_end,
        ro_data_address:      ro_data_address,
        ro_data_address_end:  ro_data_address_end,
        current_heap_pointer: current_heap_pointer,
        output_address:       output_address,
        output_end:           output_end,
        stack:                make([]byte, p_s),
        rw_data:              make([]byte, rw_data_address_end-rw_data_address),
        ro_data:              make([]byte, ro_data_address_end-ro_data_address),
        output:               make([]byte, a_size),
    }
}

func (ram *RAM) WriteRAMBytes(address uint32, data []byte) uint64 {
    length := uint32(len(data))
    end := address + length

    switch {
    case address >= ram.output_address && end <= ram.output_end:
        offset := address - ram.output_address
        copy(ram.output[offset:], data)
        return OK
    case address >= ram.stack_address && end <= ram.stack_address_end:
        offset := address - ram.stack_address
        copy(ram.stack[offset:], data)
        return OK
    case address >= ram.rw_data_address && end <= Z_func(ram.current_heap_pointer):
        offset := address - ram.rw_data_address
        copy(ram.rw_data[offset:], data)
        return OK
    case address >= ram.ro_data_address && end <= ram.ro_data_address_end:
        offset := address - ram.ro_data_address
        copy(ram.ro_data[offset:], data)
        return OK
    default:
        return OOB
    }
}

func (ram *RAM) ReadRAMBytes(address uint32, length uint32) ([]byte, uint64) {
    end := address + length

    if address >= ram.output_address && end <= ram.output_end {
        offset := address - ram.output_address
        if offset+length > uint32(len(ram.output)) {
            return nil, OOB
        }
        return ram.output[offset : offset+length], OK
    }

    if address >= ram.stack_address && end <= ram.stack_address_end {
        offset := address - ram.stack_address
        if offset+length > uint32(len(ram.stack)) {
            return nil, OOB
        }
        return ram.stack[offset : offset+length], OK
    }

    if address >= ram.rw_data_address && end <= Z_func(ram.current_heap_pointer) {
        offset := address - ram.rw_data_address
        if offset+length > uint32(len(ram.rw_data)) {
            return nil, OOB
        }
        return ram.rw_data[offset : offset+length], OK
    }

    if address >= ram.ro_data_address && end <= ram.ro_data_address_end {
        offset := address - ram.ro_data_address
        if offset+length > uint32(len(ram.ro_data)) {
            return nil, OOB
        }
        return ram.ro_data[offset : offset+length], OK
    }

    log.Warn("ok", "invalid ReadRAMBytes", "addr", fmt.Sprintf("%x", address), "l", length)
    return nil, OOB
}

func (ram *RAM) allocatePages(startPage uint32, count uint32) {
    required := (startPage + count) * Z_P
    if uint32(len(ram.rw_data)) < required {
        // Grow rw_data to fit new allocation
        newData := make([]byte, required)
        copy(newData, ram.rw_data)
        ram.rw_data = newData
    }
}
```
