# State Transition Function Test Vectors

## STF Output

Technically, the STF execution process does not inherently produce auxiliary
outputs beyond the success or failure result. In this context, we propose
an extension to include additional information that may be beneficial for
implementors or useful for executing other subsystems reliant on values
generated post-STF execution.

When the error or success values are not pertinent to your test vector
processing procedures, you may disregard them as necessary.

A mapping of error code semantics is provided within the ASN.1 schema for each
specific subsystem.

## Vectors

- [Safrole](./safrole/README.md)
- [Disputes](./disputes/README.md)
- [History](./history/README.md)
- [Assurances](./assurances/README.md)
- [Reports](./reports/README.md)
- [Statistics](./statistics/README.md)
- [Authorizations](./authorizations/README.md)
- [Preimages](./preimages/README.md)
- [Accumulate](./accumulate/README.md)

