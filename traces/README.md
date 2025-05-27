# Block Import Traces

Import full blocks starting from genesis, implementing the complete logic
required of a block importer that complies with the specifications outlined
in Graypaper Milestone 1 (M1).

## Schema

The schema is designed to be sufficiently generic to allow easy processing by
any implementation aiming to undergo conformance testing.

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./schema.asn) defined for these test cases.

## Gas Costs

The gas cost for a single instruction is set to **$1$**, unlike in GP where
it is set to $0$. This distinction is primarily intended to verify correct
tracking of gas consumption.

All host calls have a gas cost of **$10$**, with the following exceptions:
- **`transfer`**: Gas cost is set to **$10 + \omega_9$**, as specified in the GP.
- **`log`**: Gas cost is set to **0**, as defined in [JIP-1](https://hackmd.io/@polkadot/jip1).

## Vectors

- [Fallback](./fallback): fallback block authoring, no-safrole, no-work-reports
- [Safrole](./safrole): safrole block authoring, no-work-reports
- [Work Reports L0](./reports-l0): no-safrole, basic work reports (read/write/info/log)
