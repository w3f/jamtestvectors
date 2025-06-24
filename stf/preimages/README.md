# Preimages STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./preimages.asn) defined for these test cases.

## Statistics

A subset of service activity statistics ($π_S$) updated by the STF subsystem used
to process these test vectors.

In particular the `provided-count` (p.0) and `provided-size` (p.1) items are
updated when new preimages are provided to be included in the chain storage via
the extrinsic.

## Vectors

- [preimage_needed-1](./tiny/preimage_needed-1.json) 🟢
  - Nothing is provided.
- [preimage_needed-2](./tiny/preimage_needed-2.json) 🟢
  - Provide one solicited blob.
- [preimage_not_needed-1](./tiny/preimage_not_needed-1.json) 🔴
  - Provide two blobs, but one of them has not been solicited.
- [preimage_not_needed-2](./tiny/preimage_not_needed-2.json) 🔴
  - Provide two blobs, but one of them has already been provided.
- [preimages_order_check-1](./tiny/preimages_order_check-1.json) 🔴
  - Bad order of services.
- [preimages_order_check-2](./tiny/preimages_order_check-2.json) 🔴
  - Bad order of images for a service.
- [preimages_order_check-3](./tiny/preimages_order_check-3.json) 🟢
  - Order is correct.
- [preimages_order_check-4](./tiny/preimages_order_check-4.json) 🔴
  - Duplicate item.
