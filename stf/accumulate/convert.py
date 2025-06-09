#!/usr/bin/env python3

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../../lib')))

from accumulate import AccumulateTestVector # noqa: E402
from bin_to_json import convert_group # noqa: E402

os.chdir(script_dir)

for spec in ["tiny", "full"]:
    convert_group("accumulate", spec, AccumulateTestVector)
