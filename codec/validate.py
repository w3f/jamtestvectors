#!/usr/bin/env python

from pathlib import Path
import asn1tools
import os
import sys

# Get script directory before changing working directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change to script directory
os.chdir(script_dir)
print(script_dir)
target_path = os.path.join(script_dir, '../jam-types-asn')
print(target_path)
abs_path = os.path.abspath(target_path)
print(abs_path)
sys.path.append(abs_path)
print(sys.path)
exit(0)

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
target_path = os.path.join(script_dir, '../jam-types-asn')
print(target_path)
sys.path.append(os.path.abspath(target_path))
print(sys.path)


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jam-types-asn')))

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
