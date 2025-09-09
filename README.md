# Test Vectors for the JAM Protocol (0.7.0)

## Classes

- [Codec](./codec/README.md)
- [Erasure Coding](./erasure/README.md)
- [State Transition Function](./stf/README.md)
- [Block Import Traces](./traces/README.md)

## Binary To JSON

The repository binary test vector files can be converted to their JSON
equivalents for easier inspection and debugging. Use the provided conversion
script to transform binary files into human-readable JSON format:

```bash
./scripts/convert-all.sh
```

This script requires the [jam-types](https://github.com/davxy/jam-types-py)
Python library to be installed.

## Validation

Validation scripts are included to verify the JSON files against the expected
ASN.1 syntax provided with the test vectors. These scripts currently rely on my
[asn1tools](https://github.com/davxy/asn1tools) fork.

```bash
./scripts/validate-all.sh.sh
```

## Chainspec Parameters

For more information refer to the community [docs](https://docs.jamcha.in/basics/chain-spec).

### Tiny

```yaml
chain: tiny
num_validators: 6
num_cores: 2
preimage_expunge_period: 32
slot_duration: 6
epoch_duration: 12
contest_duration: 10
tickets_per_validator: 3
max_tickets_per_extrinsic: 3
rotation_period: 4
num_ec_pieces_per_segment: 1026
max_block_gas: 20000000
max_refine_gas: 1000000000
```

### Full

All parameters here must match the Gray Paper.

```yaml
chain: full
num_validators: 1023
num_cores: 341
preimage_expunge_period: 19200
slot_duration: 6
epoch_duration: 600
contest_duration: 500
tickets_per_validator: 2
max_tickets_per_extrinsic: 16
rotation_period: 10
num_ec_pieces_per_segment: 6
max_block_gas: 3500000000
max_refine_gas: 5000000000
```
