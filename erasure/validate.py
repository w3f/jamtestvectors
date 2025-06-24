#!/usr/bin/env python

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../lib')))

from validate_asn1 import validate_group  # noqa: E402

os.chdir(script_dir)

for spec in ["tiny", "full"]:
    validate_group("erasure", "schema.asn", spec)
