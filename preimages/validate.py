#!/usr/bin/env python

import asn1tools
import glob
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../jam-types-asn')))

from utils import get_schema_files, validate  # noqa: E402

os.chdir(script_dir)

def validate_data():
    print("[Validating Preimages]")
    schema = asn1tools.compile_files(get_schema_files() + ["preimages.asn"], codec="jer")
    for json_file in glob.glob("data/*.json"):
        validate(schema, json_file, "TestCase")

validate_data()
