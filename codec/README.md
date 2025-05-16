# JAM Codec Test Vectors

The test vectors are provided with a corresponding JSON file that describes
their content.

They are provided for a tiny validator set (6), epoch duration (12) and core count (2).

Both binary and json formats conform to the provided ASN.1 [schema](../asn1-schema/README.md).

## Variable-Length encoding

The JAM Codec is very similar to the SCALE encoding format, with the
main distinction lying in the compact encoding of integers

We use this variable-length encoding exclusively for the prefix of
variable-length sequences.

Although this may not be explicitly stated for some internal types within the
encoded structures, we follow the guideline from the GP that immediately follows
the variable-length definition. The relevant sentence is as follows:

> *Note that at present this is utilized only in encoding the length prefix of variable-length sequences.*

For detailed information, please refer to Appendix C of the GP.

## Semantic Correctness

These test vectors are designed to be syntactically correct only.

The content within the vectors is largely populated with random data, and the
constraints specified by the GP are intentionally not adhered to. As a result,
some vectors may contain entries that conflict with the protocol rules.

This is by design and is not relevant for the purpose of testing the codec's
handling of the data structures required by the protocol.

Protocol logic constraints are validated through dedicated STF test vectors and
any other future vectors focused on logic testing.

## Vectors

- [refine_context](data/refine_context.json)
- [work_item](data/work_item.json)
- [work_package](data/work_package.json)
- [work_result_0](data/work_result_0.json)
- [work_result_1](data/work_result_1.json)
- [work_report](data/work_report.json)
- [tickets_extrinsic](data/tickets_extrinsic.json)
- [disputes_extrinsic](data/disputes_extrinsic.json)
- [preimages_extrinsic](data/preimages_extrinsic.json)
- [assurance_extrinsic](data/assurances_extrinsic.json)
- [guarantees_extrinsic](data/guarantees_extrinsic.json)
- [header_0](data/header_0.json)
- [header_1](data/header_1.json)
- [extrinsic](data/extrinsic.json)
- [block](data/block.json)
