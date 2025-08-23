# Test Vectors for the JAM Protocol (0.6.7)

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
