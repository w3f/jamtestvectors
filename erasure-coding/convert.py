#!/usr/bin/env python3

import os
import sys
from jam_types import Struct, ByteSequence
from jam_types import class_name as n

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../lib')))
from bin_to_json import convert_group # noqa: E402

os.chdir(script_dir)

class ErasureTestVector(Struct):
    type_mapping = [
        ("data", n(ByteSequence)),
        ("shards", "Vec<ByteSequence>"),
    ]

for spec_name in ["tiny", "full"]:
    convert_group("erasure", spec_name, ErasureTestVector)
