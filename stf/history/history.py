from bin_to_json import StfTestVector
from jam_types import (
    HeaderHash,
    Null,
    OpaqueHash,
    ReportedWorkPackage,
    Struct,
    Vec,
    RecentBlocks,
)
from jam_types import class_name as n


class ReportedWorkPackages(Vec):
    sub_type = n(ReportedWorkPackage)
  
class HistoryState(Struct):
    type_mapping = [
        # The most recent blocks information (𝛽)
        ('beta', n(RecentBlocks))
    ]

class HistoryInput(Struct):
    type_mapping = [
        ('header_hash', n(HeaderHash)),
        ('parent_state_root', n(OpaqueHash)),
        ('accumulate_root', n(OpaqueHash)),
        ('work_packages', n(ReportedWorkPackages))
    ]

class HistoryOutput(Null):
    pass

class HistoryTestVector(StfTestVector):
    state_class = n(HistoryState)
    input_class = n(HistoryInput)
    output_class = n(HistoryOutput)
