#!/usr/bin/env python
 
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../../lib')))

from disputes import DisputesTestVector # noqa: E402
from bin_to_json import convert_group # noqa: E402

os.chdir(script_dir)

for spec in ["tiny", "full"]:
    convert_group("disputes", spec, DisputesTestVector)
