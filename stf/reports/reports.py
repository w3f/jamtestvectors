from bin_to_json import StfTestVector
from jam_types import (
    AuthPools,
    AvailabilityAssignments,
    EntropyBuffer,
    Enum,
    Errno,
    GuaranteesXt,
    SegmentTreeRoot,
    ServiceId,
    ServiceInfo,
    Struct,
    TimeSlot,
    ValidatorsData,
    WorkPackageHash,
    CoresStatistics,
    ServicesStatistics,
    BlockInfo,
    Vec
)
from jam_types import class_name as n


class ReportsBlocksInfo(Vec):
    sub_type = n(BlockInfo)

class ReportsAccountMapData(Struct):
    type_mapping = [
        ('service', n(ServiceInfo)),
    ]

class ReportsAccountMapEntry(Struct):
    type_mapping = [
        ('id', n(ServiceId)),
        ('data', n(ReportsAccountMapData))
    ]

class ReportsState(Struct):
    type_mapping = [
        ('avail_assignments', n(AvailabilityAssignments)),
        ('curr_validators', n(ValidatorsData)),
        ('prev_validators', n(ValidatorsData)),
        ('entropy', n(EntropyBuffer)),
        ('offenders', 'Vec<Ed25519Public>'),
        ('recent_blocks', n(ReportsBlocksInfo)),
        ('auth_pools', n(AuthPools)),
        ('accounts', 'Vec<ReportsAccountMapEntry>'),
        ('cores_statistics', n(CoresStatistics)),
        ('services_statistics', n(ServicesStatistics))
    ]  

class ReportsInput(Struct):
    type_mapping = [
        ('guarantees', n(GuaranteesXt)),
        ('slot', n(TimeSlot)),
        ('known_packages', "Vec<WorkPackageHash>"),
    ]

class ReportedItem(Struct):
    type_mapping = [
        ('work_package_hash', n(WorkPackageHash)),
        ('segment_tree_root', n(SegmentTreeRoot))
    ]

class ReportsOutputData(Struct):
    type_mapping = [
        ('reported', 'Vec<ReportedItem>'),
        ('reporters', 'Vec<Ed25519Public>')
    ]

class ReportsOutput(Enum):
    type_mapping = {
        0: ('ok', n(ReportsOutputData)),
        1: ('err', n(Errno))
    }


class ReportsTestVector(StfTestVector):
    state_class = 'ReportsState'
    input_class = 'ReportsInput'
    output_class = 'ReportsOutput'
    errno_map = {
        0: "bad_core_index",
        1: "future_report_slot",
        2: "report_epoch_before_last",
        3: "insufficient_guarantees",
        4: "out_of_order_guarantee",
        5: "not_sorted_or_unique_guarantors",
        6: "wrong_assignment",
        7: "core_engaged",
        8: "anchor_not_recent",
        9: "bad_service_id",
        10: "bad_code_hash",
        11: "dependency_missing",
        12: "duplicate_package",
        13: "bad_state_root",
        14: "bad_beefy_mmr_root",
        15: "core_unauthorized",
        16: "bad_validator_index",
        17: "work_report_gas_too_high",
        18: "service_item_gas_too_low",
        19: "too_many_dependencies",
        20: "segment_root_lookup_invalid",
        21: "bad_signature",
        22: "work_report_too_big",
     }
