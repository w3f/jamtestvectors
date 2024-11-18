#!/usr/bin/env python

import os
import sys
from pathlib import Path

import asn1tools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../asn1-schema')))
from utils import get_schema_files, validate


# # Makes the SEQUENCE of OPTIONAL values ASN.1 compliant (using CHOICE)
# def tweak_sequence_options(state_obj):
#     items = state_obj['rho']
#     for i in range(len(items)):
#         if items[i] is None:
#             items[i] = {"none": None}
#         else:
#             items[i] = {"some": items[i]}
#     return state_obj


def tweak_callback(json_obj):
    # json_obj['pre-state'] = tweak_sequence_options(json_obj['pre-state'])
    # json_obj['post-state'] = tweak_sequence_options(json_obj['post-state'])
    return json_obj


# Validate tiny
schema = asn1tools.compile_files(get_schema_files(False) + ["reports.asn"], codec="jer")
for path in Path("tiny").iterdir():
    if path.is_file() and path.suffix == ".json":
        validate(schema, path, "TestCase", tweak_callback)

# Validate full
schema = asn1tools.compile_files(get_schema_files(True) + ["reports.asn"], codec="jer")
for path in Path("full").iterdir():
    if path.is_file() and path.suffix == ".json":
        validate(schema, path, "TestCase", tweak_callback)
