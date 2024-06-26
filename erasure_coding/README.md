# Erasure coding test vectors

## Format

Each file under `vectors` directory is a json with:
- "data": the erasure encoded data. Currently random bytes to avoid having to change data if package format move (actualy data does not matter).
- "chunks": the data erasure coded between 1023 participant. 341 first chunk are from original data. Chunk size is aligned to 64 bytes. Last chunk is padded to 64 bytes with 0.
Left empty in some case see `TODO`.
- "chunks_root": EC root calculated from "chunks".
- "segments": contains 12 bytes subshards of earch 4096 byte segment of the input data. 342 first subshards are from the segments original data padded with 8 bytes. Next 684 subshards of each segments are recovery subshards.
- "segments_root": using up to 2048 32 byte segment hashes from start of data, this is the calculated root. (using segments hashes and hashes of page proofs build from those segments).
- all byte data is base64 encoded with padding (a bit ugly in subshards).
- 'vector_schema.json' is the corresponding json schema.

## Vector check

- "chunks" produce from data matches the ones in the json.
- "subshards" produce from data matcehs the ones from the json.
## NOTES

- chunks are recoverable from any 341 chunks.
- subshards allow recovering an segment from any 342 subshards.
- subshards recovery can be parallelized when their indexes are matching for multiple segments but this is implementation/optimization detail.
- when data is smaller than 21_824 bytes, current library don't allow us to do EC (can be done but it seems somehow better not to modify dependency).

## TODO

- manage "chunks" for data smaller than 21_824. Is `Chunk size is aligned to 64 bytes` actually correct?
- I only used rather small vector, maybe biggers?
- construction of segments root is valid ? I just concatenate the segments hash and the root of pages of hashes to build this.
- binary tree implementation may not be aligned with spec, it follows existing code (pad with 0 hashes up to next power of 2 and does hash internally against those hashes which is not strictly necessary). TODO not using $leaf or $node from spec appendix.
- The export subshards are fix size to 6 point (12 bytes), so the vector for a single point (684 data size) is padded with 0. This comes from the fact that implementation runs over 4104 chunks and not 684. TODO switch to align on 684 ?

## Changelog

### v0.1
   * Initial test vectors.
