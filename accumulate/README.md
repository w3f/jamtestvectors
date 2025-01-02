# Accumulate STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and a shorter epoch duration (12).
- Full: These vectors use production validators count (1023) and epoch duration (600).

Both JSON and SCALE formats conform to the JAM ASN.1 [schema](../jam-types-asn/jam-types.asn)
and this subsystem STF specific [schema](./accumulate.asn).

## Services Accounts

TODO

### Test Service Code

The test vectors invoke the `accumulate` method of the provided [test-service](./test-service).  

The PVM binary, which refers to the compiled version of the `test-service`, is
generated using the [`jam-pvm-build`](https://crates.io/crates/jam-pvm-build)
tool.

Due to differences in dependencies and compiler versions, the resulting binary
artifact frequently varies, even when generated from identical source code. As
a result, you can just rely on the code blob embedded in the test vectors, which
is available within the `accounts` map.

## Tiny Vectors

TODO

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
