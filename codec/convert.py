#!/usr/bin/env python3
#
# Convert SCALE encoded test vectors to JSON.
#
# Depends on: [jam_types](https://github.com/davxy/jam-types)

import argparse
import json
import sys

from jam_types import (
    AssurancesXt,
    Block,
    Culprit,
    DisputesXt,
    Extrinsics,
    Fault,
    GuaranteesXt,
    Header,
    PreimagesXt,
    RefineContext,
    TicketsXt,
    Verdict,
    WorkItem,
    WorkPackage,
    WorkPackageAvailSpec,
    WorkReport,
    WorkResult,
)
from scalecodec import ScaleBytes

# Map the subsystem's parameter to the corresponding dump class
dump_classes = {
    "refine_context": RefineContext,
    "work_item": WorkItem,
    "work_package": WorkPackage,
    "work_package_avail_spec": WorkPackageAvailSpec,
    "work_result": WorkResult,
    "work_report": WorkReport,
    "header": Header,
    "verdict": Verdict,
    "culprit": Culprit,
    "fault": Fault,
    "tickets_extrinsic": TicketsXt,
    "disputes_extrinsic": DisputesXt,
    "preimages_extrinsic": PreimagesXt,
    "assurances_extrinsic": AssurancesXt,
    "guarantees_extrinsic": GuaranteesXt,
    "extrinsic": Extrinsics,
    "block": Block,
}

def main():
    parser = argparse.ArgumentParser(description='STF execution dump SCALE to JSON')
    parser.add_argument('filename', type=str, help='File dump to parse')
    parser.add_argument('--type', type=str, required=True, choices=dump_classes.keys(), help='Type to parse')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    with open(args.filename, 'rb') as file:
        blob = file.read()
        scale_bytes = ScaleBytes(blob)
        dump = dump_classes[args.type](data=scale_bytes)
        decoded = dump.decode()
        print(json.dumps(decoded, indent=4))

if __name__ == '__main__':
    main()
