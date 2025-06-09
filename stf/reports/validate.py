#!/usr/bin/env python

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../../lib')))

from validate_asn1 import validate_group  # noqa: E402

os.chdir(script_dir)

# Makes the SEQUENCE of OPTIONAL values ASN.1 compliant (using CHOICE)
def tweak_assignments_sequence_of_options(state_obj):
    items = state_obj['avail_assignments']
    for i in range(len(items)):
        if items[i] is None:
            items[i] = {"none": None}
        else:
            items[i] = {"some": items[i]}

# Makes the SEQUENCE of OPTIONAL values ASN.1 compliant (using CHOICE)
def tweak_mmr_sequence_of_options(state_obj):
    for entry in state_obj['recent_blocks']:
        peaks = entry['mmr']['peaks']
        for i in range(len(peaks)):
            if peaks[i] is None:
                peaks[i] = {"none": None}
            else:
                peaks[i] = {"some": peaks[i]}
    return state_obj

def tweak_callback(json_obj):
    tweak_assignments_sequence_of_options(json_obj['pre_state'])
    tweak_mmr_sequence_of_options(json_obj['pre_state'])
    tweak_assignments_sequence_of_options(json_obj['post_state'])
    tweak_mmr_sequence_of_options(json_obj['post_state'])
    return json_obj

for spec in ["tiny", "full"]:
    validate_group("reports", "reports.asn", spec, tweak_callback)
