#!/usr/bin/env python3
#
# Convert SCALE encoded test vectors to JSON.
#
# Depends on [`jam_types`](https://github.com/davxy/jam-types)

import argparse
import sys
import json
from scalecodec import ScaleBytes

# Import the specific modules
from safrole import SafroleDump
from disputes import DisputesDump
from history import HistoryDump
from reports import ReportsDump
from assurances import AssurancesDump
from statistics import StatisticsDump
from authorizations import AuthorizationsDump
from preimages import PreimagesDump
from accumulate import AccumulateDump

# Map the subsystem's parameter to the corresponding dump class
dump_classes = {
    'safrole': SafroleDump,
    'disputes': DisputesDump,
    'history': HistoryDump,
    'reports': ReportsDump,
    'assurances': AssurancesDump,
    'statistics': StatisticsDump,
    'authorizations': AuthorizationsDump,
    'preimages': PreimagesDump,
    'accumulate': AccumulateDump,
}

def main():
    parser = argparse.ArgumentParser(description='STF execution dump SCALE to JSON')
    parser.add_argument('filename', type=str, help='File dump to parse')
    parser.add_argument('--subsystem', type=str, required=True, choices=dump_classes.keys(), help='Subsystem dump to parse')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    with open(args.filename, 'rb') as file:
        blob = file.read()
        scale_bytes = ScaleBytes(blob)
        dump = dump_classes[args.subsystem](data=scale_bytes)
        decoded = dump.decode()
        print(json.dumps(decoded, indent=4))

if __name__ == '__main__':
    main()
