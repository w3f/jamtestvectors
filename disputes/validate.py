#!/usr/bin/env python3

from pathlib import Path
import asn1tools
import json
import sys

# Makes the SEQUENCE of OPTIONAL values ASN.1 compliant (using CHOICE)
def tweak_sequence_options(state_obj):
    items = state_obj['rho']
    for i in range(len(items)):
        if items[i] is None:
            items[i] = {"none": None}
        else:
            items[i] = {"some": items[i]}
    return state_obj

# - JSON uses snake case, ASN.1 requires kebab case
# - JSON prefix octet strings with '0x', ASN doesn't like it
def make_asn1_parsable(json_str):
    json_str = json_str.replace('_', '-').replace('0x', '')
    # tweak sequence of options
    json_obj = json.loads(json_str)
    json_obj['pre-state'] = tweak_sequence_options(json_obj['pre-state'])
    json_obj['post-state'] = tweak_sequence_options(json_obj['post-state'])
    json_str = json.dumps(json_obj, indent=4)
    return json_str


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
    schema = asn1tools.compile_files(["disputes.asn", "tiny.asn"], codec="jer")
    for path in Path("tiny").iterdir():
        if path.is_file() and path.suffix == ".json":
            validate_case(schema, path)

    # Validate full
    schema = asn1tools.compile_files(["disputes.asn", "full.asn"], codec="jer")
    for path in Path("full").iterdir():
        if path.is_file() and path.suffix == ".json":
            validate_case(schema, path)

main()
