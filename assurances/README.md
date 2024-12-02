# Work Reports STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and cores count (2). They are provided in both JSON format for easy inspection and modification,
  and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators (1023) and cores count (341)
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the JAM types ASN.1 [schema](../jam-types-asn/jam-types.asn)
and the Assurances test vectors specific [schema](./assurances.asn).

## STF Output

Technically, the STF execution process does not inherently produce auxiliary
outputs beyond the success or failure result. In this context, we propose
an extension to include additional information that may be beneficial for
implementors or useful for executing other subsystems reliant on values
generated post-STF execution.

When the error or success values are not pertinent to your test vector
processing procedures, you may disregard them as necessary.

A mapping of error code semantics is provided within the ASN.1 schema for this
subsystem.

## Tiny Vectors

- TODO

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
