#!/usr/bin/env python3
#
# Convert SCALE encoded test vectors to JSON.
#
# Depends on: [jam_types](https://github.com/davxy/jam-types)

import argparse
import json
import sys

from jam_types import Struct, ByteSequence, ScaleBytes
from jam_types import class_name as n

class EcTestVector(Struct):
    type_mapping = [
        ("data", n(ByteSequence)),
        ("shards", "Vec<ByteSequence>"),
    ]

def main():
    parser = argparse.ArgumentParser(description='Converts erasure-coding binary test vector to json')
    parser.add_argument('filename', type=str, help='File dump to parse')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    with open(args.filename, 'rb') as file:
        blob = file.read()
        scale_bytes = ScaleBytes(blob)
        dump = EcTestVector(data=scale_bytes)
        decoded = dump.decode()
        print(json.dumps(decoded, indent=4))

if __name__ == '__main__':
    main()
