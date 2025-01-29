# Erasure Coding Test Vectors

This document provides test vectors for Reed-Solomon Erasure Coding based on different chain specification configurations. The current version follows the Erasure Coding standard as defined in GP 0.5.4.

## Overview
Erasure Coding is a method used for data redundancy and fault tolerance. It divides data into multiple shards and adds parity shards to allow data recovery in case of failures. The number of total, data, and parity shards varies depending on the chain specification.

## Chain Specification Parameters
The following table outlines different chain specifications and their respective parameters:

| Chain Spec | Total Shards | Data Shards | Parity Shards |
|------------|--------------|-------------|---------------|
| Tiny       | 6            | 2           | 4             |
| Full       | 1023         | 341         | 682           |

## Usage
These test vectors can be used for testing Reed-Solomon encoding and decoding implementations in blockchain storage or distributed systems. By adjusting the chain specification, one can simulate different levels of data redundancy and resilience.

## References
For more information, refer to the [Chain-Spec Documentation](https://docs.jamcha.in/basics/chain-spec).