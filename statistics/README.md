# Validators Statistics STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./statistics.asn) defined for these test cases.

## Validators Statistics

These vectors exclusively contribute to updating validator-related statistics
($π_V$ and $π_L$).

In contrast, service and core statistics ($π_S$ and $π_C$) are updated by
vectors that more directly influence the state changes relevant to those
metrics (i.e. see [preimages](../preimages/README.md#statistics),
[reports](../reports/README.md#statistics) and
[accumulate](../accumulate/README.md#statistics)).

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
