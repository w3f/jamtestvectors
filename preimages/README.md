# Preimages STF Test Vectors

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./preimages.asn).

## Vectors

- [preimage_needed-1.json](./data/preimage_needed-1.json) 🟢
  - Nothing is provided.
- [preimage_needed-2.json](./data/preimage_needed-2.json) 🟢
  - Provide one solicited blob.
- [preimage_not_needed-1.json](./data/preimage_not_needed-1.json) 🔴
  - Provide two blobs, but one of them has not been solicited.
- [preimage_not_needed-2.json](./data/preimage_not_needed-2.json) 🔴
  - Provide two blobs, but one of them has already been provided.
