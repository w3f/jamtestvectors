from bin_to_json import StfTestVector
from jam_types import (
    Extrinsics,
    Null,
    ValidatorsStatistics,
    Struct,
    TimeSlot,
    ValidatorIndex,
    ValidatorsData,
)
from jam_types import class_name as n


class StatisticsState(Struct):
    type_mapping = [
        # [π_V] Current validators statistics.
        ('vals_curr_stats', n(ValidatorsStatistics)),
        # [π_L] Last validators statistics.
        ('vals_last_stats', n(ValidatorsStatistics)),
        # [τ] Last block timeslot.
        ('slot', n(TimeSlot)),
        # [κ'] Active validators.
        ('curr_validators', n(ValidatorsData)),
    ]

class StatisticsInput(Struct):
    type_mapping = [
        # [H_t] Block timeslot.
        ('slot', n(TimeSlot)),
        # [H_i] Block author index.
        ('author_index', n(ValidatorIndex)),
        # [E] Extrinsics.
        ('extrinsic', n(Extrinsics)),
    ]

class StatisticsOutput(Null):
    pass

class StatisticsTestVector(StfTestVector):
    state_class = n(StatisticsState)
    input_class = n(StatisticsInput)
    output_class = n(StatisticsOutput)
