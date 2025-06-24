#!/usr/bin/env python

import os
import sys
from pathlib import Path
import asn1tools

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))

from validate_asn1 import get_schema_files, validate # noqa: E402

os.chdir(script_dir)

schema = asn1tools.compile_files(get_schema_files(False) + ["schema.asn"], codec="jer")

def validate_dir(dir):
    for filename in Path(dir).iterdir():
        if filename.is_file() and filename.suffix == ".json":
            if filename.name == "genesis.json":
                validate(schema, filename, "Genesis")
            else:
                validate(schema, filename, "TraceStep")
        elif filename.is_dir():
            print("[VALIDATING: '{}']".format(filename))
            validate_dir(filename)

validate_dir(".")
