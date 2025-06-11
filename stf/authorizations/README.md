# Authorizations STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./authorizations.asn) defined for these test cases.

## Guarantees Extrinsic Input

Each item in the Guarantees Extrinsic ($E_G$) contains numerous fields
that are not directly relevant for advancing the authorizations subsystem's
STF. Since these fields would only be populated with placeholder data in this
context, we opted to select only the essential fields from each $E_G$ item
to construct what we refer to as the `CoreAuthorizer`, ensuring the input
remains clear and concise.

For $g \equiv E_G[i]$, the corresponding `CoreAuthorizer` is constructed as follows:

```plaintext
CoreAuthorizer {
    core: g.w.c,      // work report core
    auth-hash: g.w.a  // work report authorizer hash
}
```

This mapping is explicitly defined in the `CoreAuthorizers` section of the
authorizations ASN.1 schema.

In the following vectors, when we refer to "guarantees," we are specifically
referencing the corresponding `CoreAuthorizer`s extracted from $E_G$.

## Tiny Vectors

- [progress_authorizations-1](tiny/progress_authorizations-1.json)
  - No guarantees.
  - Shift auths left from both pools.
- [progress_authorizations-2](tiny/progress_authorizations-2.json)
  - Guarantees for cores 0 and 1.
  - Consume authentication from both cores pools.
- [progress_authorizations-3](tiny/progress_authorizations-3.json)
  - Guarantees for core 1.
  - Shift left authentications for core 0 pool.
  - Consume authentication for core 1 pool.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
