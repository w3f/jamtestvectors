from common import Dump
from jam_types import (
    BlockInfo,
    HeaderHash,
    Null,
    OpaqueHash,
    ReportedWorkPackage,
    Struct,
    Vec,
)
from jam_types import class_name as n


class BlocksInfo(Vec):
    sub_type = n(BlockInfo)

class ReportedWorkPackages(Vec):
    sub_type = n(ReportedWorkPackage)
  
class HistoryState(Struct):
    type_mapping = [
        # The most recent block information (𝛽)
        ('beta', n(BlocksInfo))
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

class HistoryDump(Dump):
    state_class = n(HistoryState)
    input_class = n(HistoryInput)
    output_class = n(HistoryOutput)
