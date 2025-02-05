#!/usr/bin/env python

import os
import sys
from pathlib import Path

import asn1tools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jam-types-asn')))
from utils import get_schema_files, validate


# Validate tiny/full
schema = asn1tools.compile_files(get_schema_files() + ["preimages.asn"], codec="jer")
for path in Path("data").iterdir():
    if path.is_file() and path.suffix == ".json":
        validate(schema, path, "TestCase")
