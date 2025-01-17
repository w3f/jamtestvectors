This document describes community-generated test vectors concerning Block sealing for primary (T=1) and fallback (T=0), how to interpret their fields, and how to test/verify them.

[JAM Graypaper 6.4](https://graypaper.fluffylabs.dev/#/579bd12/0eae000eae00) is the primary section being tested.

These files are contributed by [Colorful Notion (JAM DUNA)](https://github.com/jam-duna/jamtestnet) and are not official.  

## Overview

When sealing a block, as per GP Section 6, two VRF Signatures:

* H_s – the seal proof
* H_v – the entropy source proof

These proofs are produced by signing (with a VRF) various inputs (c, m) derived from the block header, ticket IDs, entropy.



## JSON Structure

Each JSON file generated has the following fields:

| **JSON Key**         | **Description**                                                                                                                                         |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bandersnatch_pub`   | Hex-encoded Bandersnatch public key of the block author. In production, you typically store just the public portion.                                    |
| `bandersnatch_priv`  | Hex-encoded Bandersnatch secret key (private key). Storing private keys in production JSON is not recommended; it is done here for debugging purposes. |
| `ticket_id`          | Hex-encoded ticket identifier used for verifying or associating with a block’s VRF entropies.                                                           |
| `attempt`            | Integer attempt number (0 or 1) | 
| `c_for_H_s`          | VRF input `c` used to generate H_s.                                                                                                                     |
| `m_for_H_s`          | VRF message `m` used to generate H_s.                                                                                                                   |
| `H_s`                | Hex-encoded proof output for H_s (the VRF signature/proof itself).                                                                                      |
| `c_for_H_v`          | VRF input `c` used to generate H_v.                                                                                                                     |
| `m_for_H_v`          | VRF message `m` used to generate H_v. (Often empty in primary epoch flows.)                                                                             |
| `H_v`                | Hex-encoded proof output for H_v (the VRF signature/proof itself).                                                                                      |
| `eta3`               | Eta_3' -- concatenated in VRF Input material.                                                                               |
| `T`                  | Integer indicator for epoch type (1 = primary epoch, 0 = fallback epoch).                                                                               |
| `header_bytes`       | Hex-encoded serialized block header bytes at the time of sealing.                                                                                       |


## Example JSON

```
{
  "bandersnatch_pub": "5e465beb01dbafe160ce8216047f2155dd0569f058afd52dcea601025a8d161d",
  "bandersnatch_priv": "51c1537c18eea5c5969cb2ae45c1224cc245de5c5b8e6e25f48fb99f2786ee05",
  "ticket_id": "0x8e05a5bd0756550a156418a51bacb7a1b67d29f76d6ca5861fa3120ae9eecffc",
  "attempt": 1,
  "c_for_H_s": "6a616d5f7469636b65745f7365616c6f6ad2224d7d58aec6573c623ab110700eaca20a48dc2965d535e466d524af2a01",
  "m_for_H_s": "c55e6c8d35e024e44b6b1a03e9bbe5d37458584039193c90e1a17ee6b10c17099adea854e17f00a35331adaec9379a896094090e7f658c0ab22f2d03b6bd40128d9a95aac99649e9a76ec5ba9bc7bbd92fda3d6cb184f33d8998d6e934a548e24dd553000000000000023b7c0ccad82e20eb02002ed27ee17fb18e6d1df22799a4d119aa9be09bac2fb0623d626b81049378ab1bb7cb7eb459a6b05e2883b7be8a94287aebefe31c009864e70c7a6304ecdc0aa6130b2f17221b9571f7c7bbcde59d8095e27a79d50f",
  "H_s": "389fde27d99986f4a3130fa4733f29f0a0ab13c125ef75f85471b11f15496068e6bc5a0a103ace2e1ee988ca214c44550f68853f483da542f643aea102edbc06f3f9fadb1621afbf76d45d7c20d7e3009a1dc083b8ca29f4bc4a29b95238c108",
  "c_for_H_v": "6a616d5f656e74726f70798e05a5bd0756550a156418a51bacb7a1b67d29f76d6ca5861fa3120ae9eecffc",
  "m_for_H_v": "",
  "H_v": "023b7c0ccad82e20eb02002ed27ee17fb18e6d1df22799a4d119aa9be09bac2fb0623d626b81049378ab1bb7cb7eb459a6b05e2883b7be8a94287aebefe31c009864e70c7a6304ecdc0aa6130b2f17221b9571f7c7bbcde59d8095e27a79d50f",
  "eta3": "6f6ad2224d7d58aec6573c623ab110700eaca20a48dc2965d535e466d524af2a",
  "T": 1,
  "header_bytes": "c55e6c8d35e024e44b6b1a03e9bbe5d37458584039193c90e1a17ee6b10c17099adea854e17f00a35331adaec9379a896094090e7f658c0ab22f2d03b6bd40128d9a95aac99649e9a76ec5ba9bc7bbd92fda3d6cb184f33d8998d6e934a548e24dd553000000000000023b7c0ccad82e20eb02002ed27ee17fb18e6d1df22799a4d119aa9be09bac2fb0623d626b81049378ab1bb7cb7eb459a6b05e2883b7be8a94287aebefe31c009864e70c7a6304ecdc0aa6130b2f17221b9571f7c7bbcde59d8095e27a79d50f389fde27d99986f4a3130fa4733f29f0a0ab13c125ef75f85471b11f15496068e6bc5a0a103ace2e1ee988ca214c44550f68853f483da542f643aea102edbc06f3f9fadb1621afbf76d45d7c20d7e3009a1dc083b8ca29f4bc4a29b95238c108"
}
```


### Verifying the Seal and Testing Block Sealing

* Read the JSON file (e.g., seals/1-0.json).
* Parse the hex-encoded fields into byte slices.

Verify Seal:
* Use the public key (bandersnatch_pub) along with the stored VRF proofs (H_s, H_v) and block header to test your block seal verifier.  Note that TWO IETF Verify checks are required, one for H_s and one for H_v.

Check your Block Sealer:
* use the supplied `bandersnatch_priv`, `ticket_id` field (if `T`=1) and `header_bytes` to compute `H_s` and `H_v`



## Development Keys

In this PR are 6 development private / public keys derived from a "key" utility that relies on programmatically generatable seeds.  All the block authoring and seals rely on these development keys.  See [key](https://github.com/jam-duna/jamtestnet/tree/main/key) for details.  

JAM implementers will likely need a working FFI into the W3F ietf library to pass this test vector and specifically pass the Safrole STF test vectors.

## Motivation

Being able to verify and generate block seals of valid blocks are a key step of M1 and M2 competence.

We generated this to support our ability to work with others with [Importblocks](https://docs.jamcha.in/testing/import-blocks) where any fuzzed block has to be resealed.

For pedagogical and pedantic completeness, rather than having H_s and H_v alone, we take a "show every intermediate step" approach in these test vectors.










