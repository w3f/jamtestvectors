# Safrole Test Vectors

For details refer to ASN.1 [schema](./safrole.asn).

## NOTES

- Error codes returned as output are not part of the spec.
- On error, post-state must match pre-state.

## TODO

- Different sets for prev, curr, next, designed validators in order to observe validators rotation.

## Vectors

- [enact-epoch-change-no-tickets-1.json](enact-epoch-change-with-no-tickets-1.json):
  - Progress from slot 0 to 1.
  - No tickets extrinsic.
- [enact-epoch-change-no-tickets-2.json](enact-epoch-change-with-no-tickets-2.json):
  - Progress from slot 1 to slot 1.
  - Fails: Timeslot must be strictly monotonic.
- [enact-epoch-change-no-tickets-3.json](enact-epoch-change-with-no-tickets-3.json):
  - Progress from slot 1 to a slot in epoch's tail.
  - No tickets mark generated (no enough ticket).
- [enact-epoch-change-no-tickets-4.json](enact-epoch-change-with-no-tickets-4.json):
  - Progress from epoch's tail to next epoch.
  - Epoch mark generated.
