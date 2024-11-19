#!/usr/bin/env python

import os
import sys
from pathlib import Path

import asn1tools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jam-types-asn')))
from utils import get_schema_files, validate


# Makes the SEQUENCE of OPTIONAL values ASN.1 compliant (using CHOICE)
def tweak_sequence_of_options(state_obj):
    for entry in state_obj['beta']:
        peaks = entry['mmr']['peaks']
        for i in range(len(peaks)):
            if peaks[i] is None:
                peaks[i] = {"none": None}
            else:
                peaks[i] = {"some": peaks[i]}
    return state_obj


def tweak_callback(json_obj):  
    tweak_sequence_of_options(json_obj['pre_state'])
    tweak_sequence_of_options(json_obj['post_state'])
    return json_obj


schema = asn1tools.compile_files(get_schema_files() + ["history.asn"], codec="jer")
for path in Path("data").iterdir():
    if path.is_file() and path.suffix == ".json":
        validate(schema, path, "TestCase", tweak_callback)
