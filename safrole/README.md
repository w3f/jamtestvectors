# Safrole Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and a shorter epoch duration (12). They are provided in both JSON format for easy inspection
  and modification, and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators count (1023) and epoch duration (600).
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the specified ASN.1 schema provided [here](./safrole.asn).

## zk-SNARK SRS

Ring proofs were constructed using a SNARK built using the the [Zcash SRS paramaters](zcash-srs-2-11-uncompressed.bin).
([powers of tau ceremony details](https://zfnd.org/conclusion-of-the-powers-of-tau-ceremony)).

For construction and usage refer to Bandersnatch vrfs spec [example](https://github.com/davxy/bandersnatch-vrfs-spec/tree/main/example).

NOTE: for "tiny" initialize the `RingContext` with `ring_size = 6`; while for full `ring size = 1023`.

## Safrole **is not** Sassafras

You can use the Sassafras [RFC](https://github.com/polkadot-fellows/RFCs/blob/main/text/0026-sassafras-consensus.md)
as a guideline provided it does not conflict with the protocol described by the *Graypaper*
If case of any discrepancy, the *Graypaper* **must** be considered the authoritative source
for the JAM protocol.

Here are some key differences:
- Safrole does not use a threshold to determine if a ticket score should be considered.
  A ticket is persisted in the state if the ticket accumulator is not full or if the
  score is lower than the highest score currently in the accumulator (which is removed
  after the new ticket is inserted).
- Safrole requires the entire ticket accumulator to be filled before it can be used.
  If not enough tickets are received, a fallback mechanism is enacted. In contrast,
  Sassafras can operate with an epoch that is only partially filled with tickets.
- In Safrole, the ticket envelope contains no additional application-specific data,
  it includes only the "attempt" and the "ring proof".

Most of these differences aim to provide a clear and concise protocol specification.

## Error Output

On STF (State Transition Function) execution error, post-state must match pre-state.

Possible error codes returned as output are not part of the specification,
feel free to ignore actual numeric values.

A map for errors codes semantics used by for the test vectors is given in the ASN.1 schema.

## Tiny Vectors

- [enact_epoch_change_with_no_tickets-1.json](./tiny/enact-epoch-change-with-no-tickets-1.json) 🟢
  - Progress by one slot.
  - Randomness accumulator is updated.

- [enact_epoch_change_with_no_tickets-2.json](./tiny/enact-epoch-change-with-no-tickets-2.json) 🔴
  - Progress from slot X to slot X.
  - Timeslot must be strictly monotonic.

- [enact_epoch_change_with_no_tickets-3.json](./tiny/enact-epoch-change-with-no-tickets-3.json) 🟢
  - Progress from a slot at the begin of the epoch to a slot in the epoch's tail.
  - Tickets mark is not generated (no enough tickets).

- [enact_epoch_change_with_no_tickets-4.json](./tiny/enact-epoch-change-with-no-tickets-4.json) 🟢
  - Progress from epoch's tail to next epoch.
  - Authorities and entropies are rotated. Epoch mark is generated.

- [skip_epochs-1](./tiny/skip-epochs-1.json) 🟢
  - Progress skipping epochs with a full tickets accumulator.
  - Tickets mark is not generated. Accumulated tickets discarded. Fallback method enacted.

- [skip_epoch_tail-1](./tiny/skip-epoch-tail-1.json) 🟢
  - Progress to next epoch by skipping epochs tail with a full tickets accumulator.
  - Tickets mark has no chance to be generated. Accumulated tickets discarded. Fallback method enacted.

- [publish_tickets_no_mark-1](./tiny/publish-tickets-no-mark-1.json) 🔴
  - Submit an extrinsic with a bad ticket attempt number.

- [publish_tickets_no_mark-2](./tiny/publish-tickets-no-mark-2.json) 🟢
  - Submit good tickets extrinsic from some authorities.

- [publish_tickets_no_mark-3](./tiny/publish-tickets-no-mark-3.json) 🔴
  - Submit one ticket already recorded in the state.

- [publish_tickets_no_mark-4](./tiny/publish-tickets-no-mark-4.json) 🔴
  - Submit tickets in bad order.

- [publish_tickets_no_mark-5](./tiny/publish-tickets-no-mark-5.json) 🔴
  - Submit tickets with bad ring proof.

- [publish_tickets_no_mark-6](./tiny/publish-tickets-no-mark-6.json) 🟢
  - Submit some tickets.

- [publish_tickets_no_mark-7](./tiny/publish-tickets-no-mark-7.json) 🔴
  - Submit tickets when epoch's lottery is over.

- [publish_tickets_no_mark-8](./tiny/publish-tickets-no-mark-8.json) 🟢
  - Progress into epoch tail, closing the epoch's lottery.
  - No enough tickets, thus no tickets mark is generated.

- [publish_tickets_no_mark-9](./tiny/publish-tickets-no-mark-9.json) 🟢
  - Progress into next epoch with no enough tickets.
  - Accumulated tickets are discarded. Epoch mark generated. Fallback method enacted.

- [publish_tickets_with_mark-1](./tiny/publish-tickets-with-mark-1.json) 🟢
  - Publish some tickets with an almost full tickets accumulator.
  - Tickets accumulator is not full yet. No ticket is dropped from accumulator.

- [publish_tickets_with_mark-2](./tiny/publish-tickets-with-mark-2.json) 🟢
  - Publish some tickets filling the accumulator.
  - Two old tickets are removed from the accumulator.

- [publish_tickets_with_mark-3](./tiny/publish-tickets-with-mark-3.json) 🟢
  - Publish some tickets with a full accumulator.
  - Some old ticket are removed to make space for new ones.

- [publish_tickets_with_mark-4](./tiny/publish-tickets-with-mark-4.json) 🟢
  - With a full accumulator, conclude the lottery.
  - Tickets mark is generated.

- [publish_tickets_with_mark-5](./tiny/publish-tickets-with-mark-5.json) 🟢
  - With a published tickets mark, progress into next epoch.
  - Epoch mark is generated. Tickets are enacted.

- [enact-epoch-change-with-padding-1](./tiny/enact-epoch-change-with-padding-1.json) 🟢
  - On epoch change we recompute the ring commitment.
  - One of the keys to be used is invalidated (zeroed out) because it belongs to the (posterior) offenders list.
  - One of the keys is just invalid (i.e. it can't be decoded into a valid Bandersnatch point).
  - Both the invalid keys are replaced with the padding point during ring commitment computation.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.
