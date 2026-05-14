from bin_to_json import StfTestVector
from jam_types import (
    AvailabilityAssignments,
    Disputes,
    DisputesXt,
    Enum,
    Errno,
    OffendersMark,
    Struct,
    TimeSlot,
    ValidatorsData,
)
from jam_types import class_name as n


class DisputesState(Struct):
    type_mapping = [
        # Disputes records (ψ)
        ('psi', n(Disputes)),
        # Availability assignments (𝜌)
        ('rho', n(AvailabilityAssignments)),
        # Timeslot (τ)
        ('tau', n(TimeSlot)),
        # Validators active in the current epoch (κ)
        ('kappa', n(ValidatorsData)),
        # Validators active in the previous epoch (λ)
        ('lambda', n(ValidatorsData))
    ]

class DisputesInput(Struct):
    type_mapping = [
        # Disputes extrinsic
        ('disputes', n(DisputesXt)),
    ]

class DisputesOutput(Enum):
    type_mapping = {
        0: ('ok', n(OffendersMark)),
        1: ('err', n(Errno))
    }

class DisputesTestVector(StfTestVector):
    state_class = n(DisputesState)
    input_class = n(DisputesInput)
    output_class = n(DisputesOutput)
    errno_map = {
        0: "already_judged",
        1: "bad_vote_split",
        2: "verdicts_not_sorted_unique",
        3: "judgements_not_sorted_unique",
        4: "culprits_not_sorted_unique",
        5: "faults_not_sorted_unique",
        7: "not_enough_faults",
        8: "culprits_verdict_not_bad",
        9: "fault_verdict_wrong",
        10: "offender_already_reported",
        11: "bad_judgement_age",
        12: "bad_validator_index",
        13: "bad_signature",
        14: "bad_guarantor_key",
        15: "bad_auditor_key"
    }
