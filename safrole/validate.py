#!/usr/bin/env python3

from pathlib import Path
import asn1tools
import json
import sys

def convert_lists_to_strings(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = convert_lists_to_strings(v)
    elif isinstance(obj, list):
        if len(obj) > 0 and all(isinstance(i, str) and len(i) == 1 for i in obj):
            obj = ''.join(obj)
        else:
            obj = [convert_lists_to_strings(i) for i in obj]
    return obj


def validate_case(schema, path):
    print("* Validating: ", path)

    # Decode from json using the schema
    json_bytes = open(path, "rb").read()
    json_str_org = json_bytes.decode('utf-8')
    # Original json uses snake case, asn1 requires kebab case
    json_str = json_str_org.replace('_', '-')
    json_bytes = json_str.encode('utf-8')
    decoded = schema.decode("Testcase", json_bytes)

    # Encode to json using the schema
    encoded = schema.encode("Testcase", decoded)
    # Original json uses snake case, asn1 requires kebab case
    json_str = encoded.decode('utf-8').replace('-', '_')
    json_obj = json.loads(json_str)
    # Strings are converted to arrays of characters,
    # map back to single string.
    json_obj = convert_lists_to_strings(json_obj)
    json_str = json.dumps(json_obj, indent = 4)

    assert (json_str.rstrip() == json_str_org.rstrip())


def main():
    # Validate tiny
    schema = asn1tools.compile_files(["safrole.asn", "tiny.asn"], codec="jer")
    for path in Path("tiny").iterdir():
        if path.is_file() and path.suffix == ".json":
            validate_case(schema, path)
    # Validate full
    schema = asn1tools.compile_files(["safrole.asn", "full.asn"], codec="jer")
    for path in Path("full").iterdir():
        if path.is_file() and path.suffix == ".json":
            validate_case(schema, path)

main()
