# Accumulate STF Test Vectors

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./accumulate.asn).

## Test Service Code

Test vectors invoke the `accumulate` method of the provided [test-service](./test-service).  

The PVM binary, which refers to the compiled version of the `test-service`, is
generated using the [`jam-pvm-build`](https://crates.io/crates/jam-pvm-build)
tool.

Due to differences in dependencies and compiler versions, the resulting binary
artifact frequently varies, even when generated from identical source code. As
a result, you can just rely on the code blob embedded in the test vectors, which
is available within the `accounts` map.

## Tiny Vectors
 
- [no_available_reports-1](./tiny/no_available_reports-1.json)
  - No reports.
- [process_one_immediate_report-1](./tiny/process_one_immediate_report-1.json)
  - Report with no dependencies.
- [enqueue_and_unlock_simple-1](./tiny/enqueue_and_unlock_simple-1.json)
  - Report with unsatisfied dependency added to the ready queue.
- [enqueue_and_unlock_simple-2](./tiny/enqueue_and_unlock_simple-2.json)
  - Report with no dependencies that resolves previous dependency.
- [enqueue_and_unlock_with_sr_lookup-1](./tiny/enqueue_and_unlock_with_sr_lookup-1.json)
  - Report with unsatisfied segment tree root dependency added to the ready queue.
- [enqueue_and_unlock_with_sr_lookup-2](./tiny/enqueue_and_unlock_with_sr_lookup-2.json)
  - Report with no dependencies that resolves previous dependency.
- [enqueue_and_unlock_chain-1](./tiny/enqueue_and_unlock_chain-1.json)
  - Two reports with unsatisfied dependencies added to the ready queue.
- [enqueue_and_unlock_chain-2](./tiny/enqueue_and_unlock_chain-2.json)
  - Two additional reports with unsatisfied dependencies added to the ready queue.
- [enqueue_and_unlock_chain-3](./tiny/enqueue_and_unlock_chain-3.json)
  - Two additional reports. One with unsatisfied dependencies, thus added to the ready queue.
  - One report is accumulated and resolves two previously enqueued reports.
- [enqueue_and_unlock_chain-4](./tiny/enqueue_and_unlock_chain-4.json)
  - Report that resolves all remaining queued dependencies.
- [enqueue_and_unlock_chain_wraps-1](./tiny/enqueue_and_unlock_chain_wraps-1.json)
  - Two reports with unsatisfied dependencies added to the ready queue.
- [enqueue_and_unlock_chain_wraps-2](./tiny/enqueue_and_unlock_chain_wraps-2.json)
  - Two additional reports, one with no dependencies and thus immediately accumulated.
  - The other is pushed to the ready queue which fills up and wraps around
    (ready queue is a ring buffer).
- [enqueue_and_unlock_chain_wraps-3](./tiny/enqueue_and_unlock_chain_wraps-3.json)
  - Two additional reports with unsatisfied dependencies pushed to the ready queue.
- [enqueue_and_unlock_chain_wraps-4](./tiny/enqueue_and_unlock_chain_wraps-4.json)
  - Two additional reports, one with no dependencies and thus immediately accumulated.
  - Three old entries in the ready queue are removed.
- [enqueue_and_unlock_chain_wraps-5](./tiny/enqueue_and_unlock_chain_wraps-5.json)
  - Report with no dependencies resolves all previous enqueued reports.
- [enqueue_self_referential-1](./tiny/enqueue_self_referential-1.json)
  - Report with direct dependency on itself.
  - This makes the report stale, but pushed to the ready queue anyway.
- [enqueue_self_referential-2](./tiny/enqueue_self_referential-2.json)
  - Two reports with indirect circular dependency.
  - This makes the reports stale, but pushed to the ready queue anyway.
- [enqueue_self_referential-3](./tiny/enqueue_self_referential-3.json)
  - Two reports. First depends on second, which depends on unseen report.
- [enqueue_self_referential-4](./tiny/enqueue_self_referential-4.json)
  - New report creates a cycle with the previously queued reports.
  - This makes the reports stale, but pushed to the ready queue anyway.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
