# Safrole Test Vectors

For schema and documentation refer to [./safrole.asn].

## NOTES

- Error codes returned as output are not part of the spec.
- On error, post-state must match pre-state.

## TODO

- Different sets for prev, curr, next, designed validators in order to observe validators rotation.


## Simple Failure

- [simple-failure-0.json](simple-failure-0.json): progress from slot 0 to 0 => KO

## Progress No-Tickets

- [progress-no-tickets-0.json](progress-no-tickets-0.json): progress from slot 0 to 1. No tickets extrinsic => OK
- [progress-no-tickets-1.json](progress-no-tickets-1.json): progress to a slot in epoch's tail. With a ticket extrinsic => KO
- [progress-no-tickets-2.json](progress-no-tickets-2.json): progress to a slot in epoch's tail. With no ticket extrinsic => OK

## Enact Epoch Change No-Tickets

- [enact-epoch-change-no-tickets-0.json](enact-epoch-change-no-tickets-0.json): progress from slot 0 to 1. No tickets extrinsic => OK
- [enact-epoch-change-no-tickets-1.json](enact-epoch-change-no-tickets-1.json): progress to a slot in epoch's tail => OK
- [enact-epoch-change-no-tickets-2.json](enact-epoch-change-no-tickets-2.json): progress to next epoch, produce epoch mark => OK
