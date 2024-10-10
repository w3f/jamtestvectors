# PVM Test Vectors, version 0.3

## How to use this

The [`programs`](./programs) directory contains `.json` files, each containing a single test.

These are meant to test the PVM function Ψ from the Graypaper's Appendix A (equation 203 from v0.2.1 of the paper).

See [schema.asn](./schema.asn) for a human-readable schema of what each of the fields mean.

See [schema.json](./schema.json) for a JSON Schema.

See [TESTCASES.md](./TESTCASES.md) for a human-readable index of all of the test cases.

## TODO

   * 100% instruction coverage
   * Tests for abnormal skip values for each instruction type
   * Tests for when the initial instruction counter (ı) starts somewhere else than 0
   * Tests involving host calls
   * Tests for invalid/malformed program blobs
   * Add bigger integration-like tests
   * More gas metering tests; proper gas cost model (current one is a placeholder)

## Changelog

### v0.3

   * Removed tests which were testing gas behavior that is not yet described in the GP:
        - `inst_load_u8_trap.json`,
        - `inst_store_u8_trap_inaccessible`
        - `inst_store_u8_trap_read_only`

### v0.2

   * Bitmask paddings are now filled with zeros, in alignment with the GP.
   * Disassemblies now end with an `invalid` instruction to signify places where
     the execution traps when going out of bounds. This is a purely cosmetic change
     to the reference disassemblies and doesn't affect the test vectors themselves.
   * The `inst_rem_signed` test was changed to make the output value non-zero.
     (The behavior is unchanged; the instruction still works the same as before.)
   * Set the initial value of the output register to a non-zero for the following tests:
     (The behavior is unchanged; the instructions still work the same as before.)
        - `inst_rem_signed_with_overflow`
        - `inst_set_greater_than_signed_imm_0`
        - `inst_set_greater_than_unsigned_imm_0`,
        - `inst_set_less_than_signed_0`
        - `inst_set_less_than_signed_imm_0`
        - `inst_set_less_than_unsigned_0`,
        - `inst_set_less_than_unsigned_imm_0`
   * Add new tests:
        - `inst_load_i16`
        - `inst_load_i8`
        - `inst_load_imm_and_jump`
        - `inst_load_indirect_i16_with_offset`
        - `inst_load_indirect_i16_without_offset`
        - `inst_load_indirect_i8_with_offset`
        - `inst_load_indirect_i8_without_offset`
        - `inst_load_indirect_u16_with_offset`
        - `inst_load_indirect_u16_without_offset`
        - `inst_load_indirect_u32_with_offset`
        - `inst_load_indirect_u32_without_offset`
        - `inst_load_indirect_u8_with_offset`
        - `inst_load_indirect_u8_without_offset`
        - `inst_load_u16`
        - `inst_load_u32`
        - `inst_store_imm_u16`
        - `inst_store_imm_u32`
        - `inst_store_imm_u8`

### v0.1

   * Initial test vectors.
