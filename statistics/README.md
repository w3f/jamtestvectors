# Statistics STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and a shorter epoch duration (12). They are provided in both JSON format for easy inspection
  and modification, and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators count (1023) and epoch duration (600).
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the JAM types ASN.1 [schema](../jam-types-asn/jam-types.asn)
and the Statistics test vectors specific [schema](./statistics.asn).

## ⚠️Extrinsic Semantic Validity

These vectors are intended just to advance the statistics of validators.
Most of the content of the extrinsic is irrelevant and primarily consists of placeholder data.

## Tiny Vectors

- [stats_with_empty_extrinsic-1](./tiny/stats_with_empty_extrinsic-1.json)

- [stats_with_epoch_change-1](./tiny/stats_with_epoch_change-1.json)

- [stats_with_some_extrinsic-1](./tiny/stats_with_some_extrinsic-1.json)


## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
