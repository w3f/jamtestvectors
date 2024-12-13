# Availability Assurances STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and cores count (2).
- Full: These vectors use production validators (1023) and cores count (341)

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./assurances.asn).

## STF Output

Technically, the STF execution process does not inherently produce auxiliary
outputs beyond the success or failure result. In this context, we propose
an extension to include additional information that may be beneficial for
implementors or useful for executing other subsystems reliant on values
generated post-STF execution.

When the error or success values are not pertinent to your test vector
processing procedures, you may disregard them as necessary.

A mapping of error code semantics is provided within the ASN.1 schema for this
subsystem.

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
