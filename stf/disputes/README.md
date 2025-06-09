# Disputes STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./disputes.asn) defined for these test cases.

## Availability Assignments

Most tests use *null* entries for state availability assignments (*rho*).
The state *rho* items are only populated, with dummy values, for the specific
tests that verify the invalidation of assignments following a verdict.

## Tiny Vectors

- [progress_with_no_verdicts-1](tiny/progress_with_no_verdicts.json) 🟢 
  - No verdicts, nothing special happens
- [progress_with_verdicts-1](tiny/progress_with_verdicts-1.json) 🔴
  - Not sorted work reports within a verdict
- [progress_with_verdicts-2](tiny/progress_with_verdicts-2.json) 🔴
  - Not unique votes within a verdict
- [progress_with_verdicts-3](tiny/progress_with_verdicts-3.json) 🔴
  - Not sorted, valid verdicts
- [progress_with_verdicts-4](tiny/progress_with_verdicts-4.json) 🟢
  - Sorted, valid verdicts
- [progress_with_verdicts-5](tiny/progress_with_verdicts-5.json) 🔴
  - Not homogeneous judgements, but positive votes count is not correct
- [progress_with_verdicts-6](tiny/progress_with_verdicts-6.json) 🟢
  - Not homogeneous judgements, results in wonky verdict
- [progress_with_culprits-1](tiny/progress_with_culprits-1.json) 🔴
  - Missing culprits for bad verdict
- [progress_with_culprits-2](tiny/progress_with_culprits-2.json) 🔴
  - Single culprit for bad verdict
- [progress_with_culprits-3](tiny/progress_with_culprits-3.json) 🔴
  - Two culprits for bad verdict, not sorted
- [progress_with_culprits-4](tiny/progress_with_culprits-4.json) 🟢
  - Two culprits for bad verdict, sorted
- [progress_with_culprits-5](tiny/progress_with_culprits-5.json) 🔴
  - Report an already recorded verdict, with culprits
- [progress_with_culprits-6](tiny/progress_with_culprits-6.json) 🔴
  - Culprit offender already in the offenders list
- [progress_with_culprits-7](tiny/progress_with_culprits-7.json) 🔴
  - Offender relative to a not present verdict
- [progress_with_faults-1](tiny/progress_with_faults-1.json) 🔴
  - Missing faults for good verdict
- [progress_with_faults-2](tiny/progress_with_faults-2.json) 🟢
  - One fault offender for good verdict
- [progress_with_faults-3](tiny/progress_with_faults-3.json) 🔴
  - Two fault offenders for a good verdict, not sorted
- [progress_with_faults-4](tiny/progress_with_faults-4.json) 🟢
  - Two fault offenders for a good verdict, sorted
- [progress_with_faults-5](tiny/progress_with_faults-5.json) 🔴
  - Report an already recorded verdict, with faults
- [progress_with_faults-6](tiny/progress_with_faults-6.json) 🔴
  - Fault offender already in the offenders list
- [progress_with_faults-7](tiny/progress_with_faults-7.json) 🔴
  - Auditor marked as offender, but vote matches the verdict.
- [progress_invalidates_avail_assignments-1](tiny/progress_invalidates_avail_assignments-1.json) 🟢
  - Invalidation of availability assignments
- [progress_with_bad_signatures-1](tiny/progress_with_bad_signatures-1.json) 🔴
  - Bad signature within the verdict judgements
- [progress_with_bad_signatures-2](tiny/progress_with_bad_signatures-2.json) 🔴
  - Bad signature within the culprits sequence
- [progress_with_invalid_keys-1](tiny/progress_with_invalid_keys-1.json) 🔴
  - Unexpected key found in the culprits sequence
- [progress_with_invalid_keys-2](tiny/progress_with_invalid_keys-2.json) 🔴
  - Unexpected key found in the faults sequence
- [progress_with_verdict_signatures_from_previous_set-1](tiny/progress_with_verdict_signatures_from_previous_set-1.json) 🟢
  - Use previous epoch validators set for verdict signatures verification
- [progress_with_verdict_signatures_from_previous_set-2](tiny/progress_with_verdict_signatures_from_previous_set-2.json) 🔴
  - Age too old for verdicts judgements

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
