# Disputes STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and a shorter epoch duration (12). They are provided in both JSON format for easy inspection
  and modification, and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators count (1023) and epoch duration (600).
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the specified ASN.1 schema provided [here](./disputes.asn).

## Error Output

On STF (State Transition Function) execution error, post-state must match pre-state.

Possible error codes returned as output are not part of the specification,
feel free to ignore actual numeric values.

A map for errors codes semantics used by for the test vectors is given in the ASN.1 schema.

## Tiny Vectors

TODO: describe

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
