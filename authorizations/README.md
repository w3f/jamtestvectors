# Authorizations STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced cores count (2)
- Full: These vectors use production cores count (341).

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./authorizations.asn).

## Tiny Vectors

- [progress_authorizations-1](tiny/progress_authorizations-1.json)
  - Progress with no guarantees
- [progress_authorizations-2](tiny/progress_authorizations-2.json)
- [progress_authorizations-3](tiny/progress_authorizations-3.json)

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
