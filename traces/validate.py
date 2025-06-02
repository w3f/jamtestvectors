#!/usr/bin/env python

import os
import sys
from pathlib import Path

import asn1tools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jam-types-asn')))
from utils import get_schema_files, validate

schema = asn1tools.compile_files(get_schema_files(False) + ["schema.asn"], codec="jer")

def validate_dir(dir):
    for path in Path(dir).iterdir():
        if path.is_file() and path.suffix == ".json":
            validate(schema, path, "TestCase")
        elif path.is_dir():
            print("[VALIDATING: '{}']".format(path))
            validate_dir(path)

validate_dir(".")
