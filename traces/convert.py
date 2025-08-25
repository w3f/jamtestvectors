#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path

from jam_types import Struct, ByteArray, ByteSequence, Block, Header, OpaqueHash, Vec, String, spec
from jam_types import class_name as n

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../lib')))
from bin_to_json import convert_to_json # noqa: E402

os.chdir(script_dir)

class TrieKey(ByteArray):
    element_count = 31

class KeyValue(Struct):
    type_mapping = [
        ('key', n(TrieKey)),
        ('value', n(ByteSequence))
    ]

class KeyValues(Vec):
    sub_type = n(KeyValue)

class RawState(Struct):
    type_mapping = [
        ('state_root', n(OpaqueHash)),
        ('keyvals', n(KeyValues))
    ]

class Genesis(Struct):
    type_mapping = [
        ('header', n(Header)),
        ('state', n(RawState))
    ]

class TraceStep(Struct):
    type_mapping = [
        ('pre_state', n(RawState)),
        ('block', n(Block)),
        ('post_state', n(RawState)),
    ]

def convert_dir(dir):
    for filename in Path(dir).iterdir():
        if filename.is_file() and filename.suffix == ".bin":
            if filename.name == "genesis.bin":
                convert_to_json(filename, Genesis)
            else:
                convert_to_json(filename, TraceStep)
        elif filename.is_dir():
            print("[CONVERTING: '{}']".format(filename))
            convert_dir(filename)

spec.set_spec("tiny")

def main():
    parser = argparse.ArgumentParser(description='Convert trace files from binary to JSON format')
    parser.add_argument('folder', nargs='?', default='.', help='Folder to convert (default: current directory)')
    args = parser.parse_args()
    
    convert_dir(args.folder)

if __name__ == "__main__":
    main()
