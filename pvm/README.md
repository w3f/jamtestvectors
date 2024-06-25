# PVM Test Vectors, version 0.1

## How to use this

The [`programs`](./programs) directory contains `.json` files, each containing a single test.

Here's an example of such a test:

```
{
  "name": "inst_add",
  "initial-regs": [0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
  "code": [0, 0, 3, 8, 121, 8, 249],
  "expected-status": "trap",
  "expected-regs": [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0]
}
```

* `name` -- a unique identifier for the test
* `initial-regs` -- the initial value of each of the 13 registers; these need to be set *before* the test program is executed
* `code` -- the code blob of the program to be executed as part of the test
* `expected-status` -- the way the program is supposed to end; currently it can be one of the following:
   - `"trap"` -- the execution ended with a trap (the `trap` instruction was executed, the execution went "out of bounds", an invalid jump was made, or an invalid instruction was executed)
   - `"halt"` -- the execution finished gracefully (a dynamic jump to address `0xffff0000` was made)
* `expected-regs` -- the expected values of each of the 13 registers *after* the test program is executed

See [TESTCASES.md](./TESTCASES.md) for a human-readable index of all of the test cases.

## Changelog

### v0.1

   * Initial test vectors.
