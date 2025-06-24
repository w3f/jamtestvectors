#!/usr/bin/env python3

import glob
import os
import re
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
    spec
)

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '../lib')))
from bin_to_json import convert_to_json # noqa: E402

os.chdir(script_dir)

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


def convert(spec_name):
    print(f"\n[Converting codec ({spec_name})]")
    spec.set_spec(spec_name)
    for filename in glob.glob(f"{spec_name}/*.bin"):
        print("* Converting ", filename)
        basename = os.path.splitext(os.path.basename(filename))[0]
        basename = re.sub(r'_\d+$', '', basename)
        class_type = dump_classes[basename]
        convert_to_json(filename, class_type)   

for spec_name in ["tiny", "full"]:
    convert(spec_name)
