# Availability Assurances STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./assurances.asn) defined for these test cases.

## Tiny Vectors

- [no_assurances-1](tiny/no_assurances-1.json)🟢
  - Progress with an empty assurances extrinsic.
- [some_assurances-1](tiny/some_assurances-1.json) 🟢
  - Several assurances contributing to establishing availability supermajority for some
    of the cores.
- [no_assurances_with_stale_report-1](tiny/no_assurances_with_stale_report-1.json) 🟢
	- Progress with an empty assurances extrinsic.
	- Stale work report assignment is removed (but not returned in the output).
- [assurances_with_bad_signature-1](tiny/assurances_with_bad_signature-1.json)🔴
  - One assurance has a bad signature.
- [assurances_with_bad_validator_index-1](tiny/assurances_with_bad_validator_index-1.json)🔴
  - One assurance has a bad validator index.
- [assurance_for_not_engaged_core-1](tiny/assurance_for_not_engaged_core-1.json)🔴
  - One assurance targets a core without any assigned work report.
- [assurance_with_bad_attestation_parent-1](tiny/assurance_with_bad_attestation_parent-1.json)🔴
  - One assurance has a bad attestation parent hash.
- [assurances_for_stale_report-1](tiny/assurances_for_stale_report-1.json)🔴
  - One assurance targets a core with a stale report.
  - We are lenient on the stale report as far as it is available.
- [assurers_not_sorted_or_unique-1](tiny/assurers_not_sorted_or_unique-1.json)🔴
  - Assurers not sorted.
- [assurers_not_sorted_or_unique-2](tiny/assurers_not_sorted_or_unique-2.json)🔴
  - Duplicate assurer.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
