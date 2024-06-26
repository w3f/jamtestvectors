# PVM Test Vectors, version 0.1

## How to use this

The [`programs`](./programs) directory contains `.json` files, each containing a single test.

These are meant to test the PVM function Ψ from the Graypaper's Appendix A (equation 203 from v0.2.1 of the paper).

See [schema.asn](./schema.asn) for a human-readable schema of what each of the fields mean.

See [schema.json](./schema.json) for a JSON Schema.

See [TESTCASES.md](./TESTCASES.md) for a human-readable index of all of the test cases.

## TODO

   * 100% instruction coverage
   * Tests for abnormal skip values for each instruction type
   * Tests for when the initial instruction counter (ı) starts somewhere else than 0
   * Tests involving host calls
   * Tests for invalid/malformed program blobs
   * Add bigger integration-like tests
   * More gas metering tests; proper gas cost model (current one is a placeholder)

## Changelog

### v0.1

   * Initial test vectors.
