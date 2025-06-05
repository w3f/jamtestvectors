#!/usr/bin/env python

from pathlib import Path
import asn1tools
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jam-types-asn')))

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
