from bin_to_json import StfTestVector
from jam_types import (
    AssurancesXt,
    AvailabilityAssignments,
    Enum,
    Errno,
    HeaderHash,
    Struct,
    TimeSlot,
    ValidatorsData,
)
from jam_types import class_name as n


class AssurancesState(Struct):
    type_mapping = [
        ('avail_assignments', n(AvailabilityAssignments)),
        ('curr_validators', n(ValidatorsData)),
    ]  

class AssurancesInput(Struct):
    type_mapping = [
        ('assurances', n(AssurancesXt)),
        ('slot', n(TimeSlot)),
        ('parent', n(HeaderHash)),
    ]

class AssurancesOutputData(Struct):
    type_mapping = [
        ('reported', 'Vec<WorkReport>'),
    ]

class AssurancesOutput(Enum):
    type_mapping = {
        0: ('ok', n(AssurancesOutputData)),
        1: ('err', n(Errno))
    }


class AssurancesTestVector(StfTestVector):
    state_class = 'AssurancesState'
    input_class = 'AssurancesInput'
    output_class = 'AssurancesOutput'
    errno_map = {
        0: "bad_attestation_parent",
        1: "bad_validator_index",
        2: "core_not_engaged",
        3: "bad_signature",
        4: "not_sorted_or_unique_assurers",
    }
