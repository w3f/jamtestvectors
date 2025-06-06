#!/usr/bin/env python

from pathlib import Path
import asn1tools
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../jam-types-asn')))
print(sys.path)

os.chdir(script_dir)

from utils import get_schema_files, validate

# Validate tiny
print("[Validating Tiny Spec]")
schema = asn1tools.compile_files(get_schema_files(False), codec="jer")
for path in Path("tiny").iterdir():
    if path.is_file() and path.suffix == ".json":
        validate(schema, path)
 
# Validate full
print("[Validating Full Spec]")
schema = asn1tools.compile_files(get_schema_files(True), codec="jer")
for path in Path("full").iterdir():
    if path.is_file() and path.suffix == ".json":
        validate(schema, path)
