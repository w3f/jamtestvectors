# Statistics STF Test Vectors

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./statistics.asn).

## ⚠️Extrinsic Semantic Validity

These vectors are intended just to advance the statistics of validators.
Most of the content of the extrinsic is irrelevant and primarily consists of placeholder data.

## Tiny Vectors

- [stats_with_empty_extrinsic-1](./tiny/stats_with_empty_extrinsic-1.json)
  - Empty extrinsic with no epoch change.
  - Only author blocks counter is incremented.
- [stats_with_epoch_change-1](./tiny/stats_with_epoch_change-1.json)
  - Misc extrinsic information with no epoch change.
  - See "Extrinsic Semantic Validity" section.
- [stats_with_some_extrinsic-1](./tiny/stats_with_some_extrinsic-1.json)
  - Misc extrinsic information with no epoch change.
  - See "Extrinsic Semantic Validity" section.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
