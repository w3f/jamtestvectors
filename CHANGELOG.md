## v0.6.6 [25-06-2025]

### Changes

- Codebase reorganization
- Binary to JSON conversion scripts and utilities
* Extended the `fetch` host call with new variants.
* Updated numeric identifiers used in `fetch`.
* Updated numeric identifiers for PVM errors.
* PVM wrangled operands changed.
* Removed the traces `000...000.bin/json` step, as it was not a valid trace step and was intended to be handled specially for genesis. Since it shared the same format as regular trace steps, it could be ambiguous or misleading. 
* Introduced an explicit `genesis.bin` file containing the genesis state and header.
* The *authorizer trace* field has been moved to the end of the accumulation operand encoding  (C.29)

### Deviations

* `fetch` host call for protocol parameters ($\omega_{10}=0$) has been implemented according to this (currently) unreleased change: https://github.com/gavofyork/graypaper/pull/414
For the `fetch` hostcall id we're still using 18 as per GP 0.6.6. The picked change only concerns the value returned for w_10=0

### Extra

* Codebase reorganization
* Binary to JSON conversion scripts and utilities
* CI: ASN.1 verification

## v0.6.5 [02-06-2025]

- First Release
