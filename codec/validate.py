#!/usr/bin/env python3

from pathlib import Path
import asn1tools
import json
import sys

import os
import re

# - JSON uses snake case, ASN.1 requires kebab case
# - JSON prefix octet strings with '0x', ASN doesn't like it
def make_asn1_parsable(json_str):
    return json_str.replace('_', '-').replace('0x', '')

def path_to_struct_name(path):
    # Strip the directory path and extension
    name = os.path.splitext(os.path.basename(path))[0]   
    # Remove "_X" if it ends with a number
    name = re.sub(r'_\d+$', '', name)   
    # Convert kebab-case or snake_case to PascalCase
    name = re.sub(r'[-_](\w)', lambda m: m.group(1).upper(), name)   
    # Capitalize the first character
    name = name[0].upper() + name[1:]   
    return name    

def validate_case(schema, path):
    print("* Validating: ", path)

    type_name = path_to_struct_name(path)

    # Decode from json using the schema
    json_bytes = open(path, "rb").read()
    json_str_org = json_bytes.decode('utf-8')
    json_str_org = make_asn1_parsable(json_str_org)
    
    json_bytes = json_str_org.encode('utf-8')
    decoded = schema.decode(type_name, json_bytes, check_constraints=True)

    # Encode to json using the schema
    encoded = schema.encode(type_name, decoded, check_constraints=True)
    # Original json uses snake case, asn1 requires kebab case
    json_str = encoded.decode('utf-8')
    json_obj = json.loads(json_str)
    # Strings are converted to arrays of characters,
    # map back to single string.
    json_str = json.dumps(json_obj, indent = 4)

    assert (json_str.rstrip().lower() == json_str_org.rstrip().lower())


def main():
    # Validate tiny
    schema = asn1tools.compile_files(["schema.asn"], codec="jer")
    for path in Path("data").iterdir():
        if path.is_file() and path.suffix == ".json":
            validate_case(schema, path)

main()
