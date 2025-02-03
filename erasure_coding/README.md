# Erasure Coding Test Vectors

This document provides test vectors for Reed-Solomon Erasure Coding based on different chain specification configurations. The current version follows the Erasure Coding standard as defined in GP 0.6.1.

## Overview

Erasure Coding is a method used for data redundancy and fault tolerance. It divides data into multiple shards and adds parity shards to allow data recovery in case of failures. The total number of data and parity shards varies depending on the chain specification.

## Data Description

In this context, `data` represents the original information before encoding, while `segment` refers to the fragments generated after applying Erasure Coding.

- Each **shard** has a length of `2 * numPieces`. Since each byte is represented by two hexadecimal characters, the total length of each shard is `2 * numPieces * 2 = 24` characters.
- Each **segment_ec** corresponds to a portion of the original data that has been split into chunks of length `2 * numPieces * data_shard`.
- If `numPieces = 6`, then:
  - Each segment will have a length of `2 * 6 * 2 = 24` characters.
  - If the original data exceeds this length, additional segments are required to store the remaining data.
  - If the data length is less than `2 * numPieces * data\_shard`, it will be padded with zeros to match the required length.

## Data Generation Description

According to the [Gray Paper](https://graypaper.fluffylabs.dev/#/4bb8fd2/1baa001b5701), Erasure Coding is used in two main scenarios:

1. **Work Package Bundle Erasure Coding**
   - The encoding scheme follows the formula: 
     ```math
     C_{\lceil |b| / W_E \rceil}\left( \mathcal{P}_{W_E} (\mathbf{b}) \right)
     ```
   - The number of GF points per shard is determined dynamically based on the size of `b`.
   - Regardless of the length of `b`, the encoding result will always produce a single set of EC shards.

2. **Segment and Page Proof Erasure Coding**
   - The encoding scheme follows the formula:
     ```math
     C_6( \mathbf{s}︿P(\mathbf{s}) )
     ```
   - Each shard contains exactly 6 GF points, equivalent to 12 bytes (24 hex characters), since:
     ```math
     1 \text{ GF Point} = 2 \text{ bytes} = 4 \text{ hex characters}
     ```
   - Given that C_6 requires a total of 342 data shards:
     ```math
     342 * 12 = 4104 = G
     ```
   - Data can be fully allocated into the data shards without waste.

## Usage

These test vectors can be used for testing Reed-Solomon encoding and decoding implementations in blockchain storage or distributed systems. By adjusting the chain specification, one can simulate different levels of data redundancy and resilience.

## References

For more information, refer to the [Gray Paper](https://graypaper.fluffylabs.dev/#/4bb8fd2/3c11003c1100).
