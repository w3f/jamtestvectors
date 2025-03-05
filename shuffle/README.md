# Fisher-Yates Shuffle function test vectors

We offer test vectors for the implementation of the shuffle function as described in Appendix F of the Gray Paper.
This section presents two definitions, a recursive one that uses an integer sequence as random seeds in Eq 329, and one (Eq 331) which takes a 32-byte hash as entropy, and is defined in terms of the previous one.

The implementation of Eq 329 is not generally used in the Gray Paper, and so we present test vectors only for the version of Eq 331. However, the present script creates these test cases with recourse to the Eq 329 implementation, to reproduce exactly the definition of the Gray Paper.

Note: All gray paper references in this document are to version 0.4.3, October 21st 2024.

## Notes about test parameters

In every case, the output must be a permutation of the input sequence, and this is checked by the generating script.
In the GP, at the moment, this function is used only to shuffle sequences of validators or cores, both of which are identified by integers. For that reason, all test cases use integers as the input type. All the input elements are distinct to ensure the final positions of each element are unambiguously determined.

All the inputs to each test case are integer sequences, ranging from 0 to n-1, where n is the length. The test cases are described only by the entropy and the length of the input, and so the actual input sequence has to be recreated when using these test cases.

## Test vectors

The following test cases are given:
- 0
- 8
- 16
- 20
- 50
- 100
- 200
- 341

Each test case has this format is a Json object with 3 fields:
* **[input]**: the length of the input sequence
* **[entropy]**: a hex-string description of the 32 bytes used for entropy
* **[output]**: an array containing the shuffled input sequence
