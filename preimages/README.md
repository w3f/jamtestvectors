# Preimages STF Test Vectors

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./preimages.asn).

## Vectors

- [preimage_needed-1](./data/preimage_needed-1.json) 🟢
  - Nothing is provided.
- [preimage_needed-2](./data/preimage_needed-2.json) 🟢
  - Provide one solicited blob.
- [preimage_not_needed-1](./data/preimage_not_needed-1.json) 🔴
  - Provide two blobs, but one of them has not been solicited.
- [preimage_not_needed-2](./data/preimage_not_needed-2.json) 🔴
  - Provide two blobs, but one of them has already been provided.
- [preimages_order_check-1](./data/preimages_order_check-1.json) 🔴
  - Bad order of services.
- [preimages_order_check-2](./data/preimages_order_check-2.json) 🔴
  - Bad order of images for a service.
- [preimages_order_check-3](./data/preimages_order_check-3.json) 🟢
  - Order is correct.
- [preimages_order_check-4](./data/preimages_order_check-4.json) 🔴
  - Duplicate item.
