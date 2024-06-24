# Safrole Test Vectors

For details refer to ASN.1 [schema](./safrole.asn).

## NOTES

- Error codes returned as output are not part of the spec.
- On error, post-state must match pre-state.
- Ring verifier is constructed using [ark-ec-vrfs](https://github.com/davxy/ark-ec-vrfs) procedures

## TODO

- Different sets for prev, curr, next, designed validators in order to observe validators rotation.
- Better specify the procedure used to construct test ring verifier.

## Vectors

- [enact-epoch-change-no-tickets-1.json](enact-epoch-change-with-no-tickets-1.json)
  - Progress from slot 0 to 1.
  - No tickets extrinsic.
- [enact-epoch-change-no-tickets-2.json](enact-epoch-change-with-no-tickets-2.json)
  - Progress from slot 1 to slot 1.
  - Fails: Timeslot must be strictly monotonic.
- [enact-epoch-change-no-tickets-3.json](enact-epoch-change-with-no-tickets-3.json)
  - Progress from slot 1 to a slot in epoch's tail.
  - Tickets mark is not generated (no enough ticket).
- [enact-epoch-change-no-tickets-4.json](enact-epoch-change-with-no-tickets-4.json)
  - Progress from epoch's tail to next epoch.
  - Authorities / entropies rotated.
  - Epoch mark generated.

- [skip-epochs-1](skip-epochs-1.json)
  - Progress by skipping epochs.
  - Accumulated tickets are discarded>
  - Tickets mark is not generated (skipped epochs).
  - Fallback method is enacted.

- [skip-epoch-tail-1](skip-epoch-tail-1.json)
  - Progress to next epoch by skipping epochs tail.
  - Tickets mark has no chance to be generated.
  - Even tough we have enough tickets, these are discarded when next epoch is enacted.
  - Fallback method is enacted.

- [publish-tickets-no-mark-1](publish-tickets-no-mark-1.json)
  - Try submit an extrinsic with more tickets than max allowed.
  - Fails.
- [publish-tickets-no-mark-2](publish-tickets-no-mark-2.json)
  - Submit tickets extrinsics from authority 0 and 1.
- [publish-tickets-no-mark-3](publish-tickets-no-mark-3.json)
  - Fail to re submit tickets from authority 0.
- [publish-tickets-no-mark-4](publish-tickets-no-mark-4.json)
  - Fail to submit tickets in bad order.
- [publish-tickets-no-mark-5](publish-tickets-no-mark-5.json)
  - Fail to submit tickets with bad ring proof.
- [publish-tickets-no-mark-6](publish-tickets-no-mark-6.json)
  - Submit a ticket from authority 2.
- [publish-tickets-no-mark-7](publish-tickets-no-mark-7.json)
  - Fail to submit a ticket while in epoch's tail.
- [publish-tickets-no-mark-8](publish-tickets-no-mark-8.json)
  - Progress into epoch tail.
  - No enough tickets, thus no tickets mark.
  - TODO: technically we can already drop the tickets from accumulator (check graypaper).
- [publish-tickets-no-mark-9](publish-tickets-no-mark-9.json)
  - Advance into next epoch.
  - Tickets are dropped.
  - Fallback method is enacted.
