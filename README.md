# Test Vectors for the JAM Protocol

## Codec
 
- [Codec](./codec/README.md)

## Erasure Coding

- [Erasure Coding](./erasure/README.md)

## State Transition Functions

We offer two types of test vectors:

- **Tiny**: designed for quick adjustments and prototyping, with reduced
  - validators count: 6
  - cores count: 2
  - epoch period: 12
  - core assignment rotation period: 4
  - ticket attempts: 3

- **Full**: vectors with production specs
  - validators count: 1023
  - cores count: 341
  - epoch period: 600
  - core assignment rotation period: 10
  - ticket attempts: 2

For more information refer to the community [docs](https://docs.jamcha.in/basics/chain-spec).

### STF Output

Technically, the STF execution process does not inherently produce auxiliary
outputs beyond the success or failure result. In this context, we propose
an extension to include additional information that may be beneficial for
implementors or useful for executing other subsystems reliant on values
generated post-STF execution.

When the error or success values are not pertinent to your test vector
processing procedures, you may disregard them as necessary.

A mapping of error code semantics is provided within the ASN.1 schema for each
specific subsystem.

### Vectors

- [Safrole](./stf/safrole/README.md)
- [Disputes](./stf/disputes/README.md)
- [History](./stf/history/README.md)
- [Assurances](./stf/assurances/README.md)
- [Reports](./stf/reports/README.md)
- [Statistics](./stf/statistics/README.md)
- [Authorizations](./stf/authorizations/README.md)
- [Preimages](./stf/preimages/README.md)
- [Accumulate](./stf/accumulate/README.md)

## Block Import Traces

- [Fallback](./traces/fallback): fallback block authoring, no-safrole, no-work-reports
- [Safrole](./traces/safrole): safrole block authoring, no-work-reports
- [Work Reports L0](./traces/reports-l0): basic work reports, no-safrole

## Vectors Validation

Validation scripts are included to verify the JSON files against the expected
ASN.1 syntax provided with the test vectors. These scripts currently rely on my
[asn1tools](https://github.com/davxy/asn1tools) fork.

## Binary To JSON

The repository binary test vector files can be converted to their JSON
equivalents for easier inspection and debugging. Use the provided conversion
script to transform binary files into human-readable JSON format:

```bash
./scripts/convert-all.sh
```

This conversion script requires the [jam-types](https://github.com/davxy/jam-types)
Python library to be installed.
