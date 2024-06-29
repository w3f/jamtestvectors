# Safrole Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and a shorter epoch duration (12). They are provided in both JSON format for easy inspection
  and modification, and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators count (1023) and epoch duration (600).
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the specified ASN.1 schema provided [here](./safrole.asn).

## NOTES

- Error codes returned as output are not part of the specification. Feel free to ignore actual values.
- On error, post-state must match pre-state.
- Ring verifier key is constructed using [ark-ec-vrfs](https://github.com/davxy/ark-ec-vrfs)
  from a `RingContext` built using a 32 zero octets seed (`[0; 32]`) and domain size of 2048.

## Tiny Vectors

- [enact-epoch-change-no-tickets-1.json](./tiny/enact-epoch-change-with-no-tickets-1.json)
  - Progress by one slot.
  - Randomness accumulator is updated.
- [enact-epoch-change-no-tickets-2.json](./tiny/enact-epoch-change-with-no-tickets-2.json)
  - Progress from slot X to slot X.
  - Fail: Timeslot must be strictly monotonic.
- [enact-epoch-change-no-tickets-3.json](./tiny/enact-epoch-change-with-no-tickets-3.json)
  - Progress from a slot at the begin of the epoch to a slot in the epoch's tail.
  - Tickets mark is not generated (no enough tickets).
- [enact-epoch-change-no-tickets-4.json](./tiny/enact-epoch-change-with-no-tickets-4.json)
  - Progress from epoch's tail to next epoch.
  - Authorities and entropies are rotated.
  - Epoch mark is generated.
- [skip-epochs-1](./tiny/skip-epochs-1.json)
  - Progress skipping epochs with a full tickets accumulator.
  - Tickets mark is not generated.
  - Accumulated tickets are discarded.
  - Fallback method is enacted.
- [skip-epoch-tail-1](./tiny/skip-epoch-tail-1.json)
  - Progress to next epoch by skipping epochs tail with a full tickets accumulator.
  - Tickets mark has no chance to be generated.
  - Accumulated tickets are discarded.
  - Fallback method is enacted.
- [publish-tickets-no-mark-1](./tiny/publish-tickets-no-mark-1.json)
  - Fail: Submit an extrinsic with a bad ticket attempt number.
- [publish-tickets-no-mark-2](./tiny/publish-tickets-no-mark-2.json)
  - Submit good tickets extrinsics from authority 0 and 1.
- [publish-tickets-no-mark-3](./tiny/publish-tickets-no-mark-3.json)
  - Fail: Re-submit tickets from authority 0 (together with tickets from authority 2).
- [publish-tickets-no-mark-4](./tiny/publish-tickets-no-mark-4.json)
  - Fail: Submit tickets in bad order.
- [publish-tickets-no-mark-5](./tiny/publish-tickets-no-mark-5.json)
  - Fail: Submit tickets with bad ring proof.
- [publish-tickets-no-mark-6](./tiny/publish-tickets-no-mark-6.json)
  - Submit tickets from authority 2.
- [publish-tickets-no-mark-7](./tiny/publish-tickets-no-mark-7.json)
  - Fail: Submit authority 3 tickets while in epoch's tail.
- [publish-tickets-no-mark-8](./tiny/publish-tickets-no-mark-8.json)
  - Progress into epoch tail.
  - No enough tickets, thus no tickets mark is generated.
- [publish-tickets-no-mark-9](./tiny/publish-tickets-no-mark-9.json)
  - Progress into next epoch with no enough tickets.
  - Accumulated tickets are discarded.
  - Epoch mark is generated.
  - Fallback method is enacted.
- [publish-tickets-with-mark-1](./tiny/publish-tickets-with-mark-1.json)
  - Publish some tickets with an almost full tickets accumulator.
  - Tickets accumulator is not full yet.
  - No ticket are dropped from accumulator.
- [publish-tickets-with-mark-2](./tiny/publish-tickets-with-mark-2.json)
  - Publish some more tickets.
  - Tickets accumulator is filled.
  - Two old ticket are removed from the accumulator.
- [publish-tickets-with-mark-3](./tiny/publish-tickets-with-mark-3.json)
  - Publish some more tickets.
  - Accumulator is full before execution.
  - Some old ticket are removed to make space for new ones.
- [publish-tickets-with-mark-4](./tiny/publish-tickets-with-mark-4.json)
  - Progress into epoch tail.
  - Tickets mark is generated.
- [publish-tickets-with-mark-5](./tiny/publish-tickets-with-mark-5.json)
  - Progress into next epoch.
  - Epoch mark is generated.
  - Tickets are enacted.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
