#!/usr/bin/env python3

from pathlib import Path
import asn1tools
import json
import sys

# - JSON uses snake case, ASN.1 requires kebab case
# - JSON prefix octet strings with '0x', ASN doesn't like it
def make_asn1_parsable(json_str):
    return json_str.replace('_', '-').replace('0x', '')

def validate_case(schema, path):
    print("* Validating: ", path)

    # Decode from json using the schema
    json_bytes = open(path, "rb").read()
    json_str_org = json_bytes.decode('utf-8')
    json_str_org = make_asn1_parsable(json_str_org)
    
    json_bytes = json_str_org.encode('utf-8')
    decoded = schema.decode("TestCase", json_bytes, check_constraints=True)

    # Encode to json using the schema
    encoded = schema.encode("TestCase", decoded, check_constraints=True)
    # Original json uses snake case, asn1 requires kebab case
    json_str = encoded.decode('utf-8')
    json_obj = json.loads(json_str)
    # Strings are converted to arrays of characters,
    # map back to single string.
    json_str = json.dumps(json_obj, indent = 4)

    assert (json_str.rstrip().lower() == json_str_org.rstrip().lower())


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
