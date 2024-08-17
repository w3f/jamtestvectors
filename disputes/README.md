# Disputes STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and a shorter epoch duration (12). They are provided in both JSON format for easy inspection
  and modification, and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators count (1023) and epoch duration (600).
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the specified ASN.1 schema provided [here](./disputes.asn).

## Error Output

On STF (State Transition Function) execution error, post-state must match pre-state.

Possible error codes returned as output are not part of the specification,
feel free to ignore actual numeric values.

A map for errors codes semantics used by for the test vectors is given in the ASN.1 schema.

## Tiny Vectors

- [progress_with_no_verdicts-1](tiny/progress_with_no_verdicts.json) 🟢 
  - No verdicts, nothing special happens

- [progress_with_verdicts-1](tiny/progress_with_verdicts-1.json) 🔴
  - Not sorted work reports within a verdict

- [progress_with_verdicts-2](tiny/progress_with_verdicts-2.json) 🔴
  - Not unique votes within a verdict

- [progress_with_verdicts-3](tiny/progress_with_verdicts-3.json)
- [progress_with_verdicts-4](tiny/progress_with_verdicts-4.json)
- [progress_with_verdicts-5](tiny/progress_with_verdicts-5.json)
- [progress_with_verdicts-6](tiny/progress_with_verdicts-6.json)

- [progress_with_faults-1](tiny/progress_with_faults-1.json)
- [progress_with_faults-2](tiny/progress_with_faults-2.json)
- [progress_with_faults-3](tiny/progress_with_faults-3.json)
- [progress_with_faults-4](tiny/progress_with_faults-4.json)
- [progress_with_faults-5](tiny/progress_with_faults-5.json)
- [progress_with_faults-6](tiny/progress_with_faults-6.json)
- [progress_with_faults-7](tiny/progress_with_faults-7.json)

- [progress_with_culprits-1](tiny/progress_with_culprits-1.json)
- [progress_with_culprits-2](tiny/progress_with_culprits-2.json)
- [progress_with_culprits-3](tiny/progress_with_culprits-3.json)
- [progress_with_culprits-4](tiny/progress_with_culprits-4.json)
- [progress_with_culprits-5](tiny/progress_with_culprits-5.json)
- [progress_with_culprits-6](tiny/progress_with_culprits-6.json)
- [progress_with_culprits-7](tiny/progress_with_culprits-7.json)

- [progress_invalidates_avail_assignments-1](tiny/progress_invalidates_avail_assignments-1.json)

- [progress_with_bad_signatures-1](tiny/progress_with_bad_signatures-1.json)
- [progress_with_bad_signatures-2](tiny/progress_with_bad_signatures-2.json)


- [progress_with_verdict_signatures_from_previous_set-1](tiny/progress_with_verdict_signatures_from_previous_set-1.json)
- [progress_with_verdict_signatures_from_previous_set-2](tiny/progress_with_verdict_signatures_from_previous_set-2.json)

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
