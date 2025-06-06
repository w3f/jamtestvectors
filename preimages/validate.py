#!/usr/bin/env python

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../jam-types-asn')))

from utils import validate_group  # noqa: E402

os.chdir(script_dir)

validate_group("preimages", "preimages.asn", "data")
