#!/usr/bin/env python

import asn1tools
import glob
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../jam-types-asn')))

from utils import get_schema_files, validate  # noqa: E402

os.chdir(script_dir)

def validate_spec(spec_name):
    print(f"[Validating '{spec_name}' spec]")
    schema = asn1tools.compile_files(get_schema_files(spec_name == "full") + ["accumulate.asn"], codec="jer")
    for json_file in glob.glob(f"{spec_name}/*.json"):
        validate(schema, json_file, "TestCase")

validate_spec("tiny")
validate_spec("full")
