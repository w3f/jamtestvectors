# Erasure coding test vectors

## Format

Each file under `vectors` directory is a json with:
- "data": Base input for different fields.

## Work package EC

files starting by "segment_root_" using "schema_segment_root.json".
- "chunks": GP-0.2.1-306-C the data erasure coded between 1023 participant. 341 first chunk are from original data. Chunk size is aligned to 64 bytes. Last chunk is padded to 64 bytes with 0.  TODO I don't find any good reference in GP to it
- "chunks_root": GP-0.2.1-290-M EC root calculated from "chunks".

Left empty in some case see `TODO`.

## Single segment EC

files starting by "ec_" using "schema_ec.json".
- "segments/segment_ec": GP-0.2.1-306-C: contains N ec point of a single segment. Size of segment is size of data. 342 first subshards are from the segments original data padded with 8 bytes. Next 684 subshards of each segments are recovery subshards.

## Segments EC

files starting by "segment_ec_" using "schema_segment_ec.json".
- "segments_root": GP-0.2.1-289-M: using up to 2048 32 byte segment hashes from start of data, this is the calculated root. (using segments hashes and hashes of page proofs build from those segments).
- "segments/segment_ec": GP-0.2.1-306-C: contains 12 bytes subshards of ec of each segments. 342 first subshards are from the segments original data padded with 8 bytes. Next 684 subshards of each segments are recovery subshards.

## Page proof of segments EC

files starting by "page_proof_" using "schema_page_proof.json".
- "page_proofs": GP-0.2.1-171-P (using GP-0.2.1-291-Jx) considering "data" contains a sequence of 4096 byte segments (last one may be unaligned).
- "segments_root": GP-0.2.1-289-M: considering "data" as a sequence of segments hashes (bounded to maximum 2^11), this contains page proofs segments.
- all byte data is base64 encoded with padding (a bit ugly in subshards).
- 'vector_schema.json' is the corresponding json schema.

## Vector check

- GP-0.2.1-307-R:  "chunks" produce from data matches the ones in the json.
- "subshards" produce from data matcehs the ones from the json.

## NOTES

- chunks are recoverable from any 341 chunks.
- subshards allow recovering an segment from any 342 subshards.
- subshards recovery can be parallelized when their indexes are matching for multiple segments but this is implementation/optimization detail.
- when data is smaller than 21_824 bytes, current library don't allow us to do EC (can be done but it seems somehow better not to modify dependency).

## TODO

- manage "chunks" for data smaller than 21_824. Is `Chunk size is aligned to 64 bytes` actually correct?
- I only used rather small vector, maybe biggers?
- construction of segments root is valid ? I just concatenate  the segments hash and the root of pages of hashes to build this.
- binary tree implementation may not be aligned with spec, it follows existing code (pad with 0 hashes up to next power of 2 and does hash internally against those hashes which is not strictly necessary). TODO not using $leaf or $node from spec appendix.
- The export subshards are fix size to 6 point (12 bytes), so the vector for a single point (684 data size) is padded with 0. This comes from the fact that implementation runs over 4104 chunks and not 684. TODO switch to align on 684 ?
- $leaf from GP-0.2.1-292 is not applied , rather not sure what it is at this point (I infer rewrite on bit of hashes to indicate if leaf, but leaf are preimage of 2048 bytes when branch are preimage of 64 byte data, so not too sure what is this $leaf).

## Changelog

### v0.1
   * Initial test vectors.
