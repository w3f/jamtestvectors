from bin_to_json import StfTestVector
from jam_types import (
    BandersnatchRingCommitment,
    BandersnatchRingVrfSignature,
    Entropy,
    EntropyBuffer,
    Enum,
    EpochMark,
    Struct,
    TicketAttempt,
    TicketBody,
    TicketEnvelope,
    TicketId,
    TicketsAccumulator,
    TicketsMark,
    TicketsOrKeys,
    TicketsXt,
    TimeSlot,
    ValidatorsData,
    Errno
)
from jam_types import class_name as n


class SafroleState(Struct):
    type_mapping = [
        # The most recent block's timeslot (τ).
        ('tau', n(TimeSlot)),
        # The entropy accumulator and epochal randomness (η).
        ('eta', n(EntropyBuffer)),
        # The validator keys and metadata which were active in the prior epoch (λ).
        ('lambda', n(ValidatorsData)),
        # The validator keys and metadata currently active (κ).
        ('kappa', n(ValidatorsData)),
        # The validator keys and metadata for the next epoch (𝛾_k).
        ('gamma_k', n(ValidatorsData)),
        # The validator keys and metadata to be drawn from next (ι).
        ('iota', n(ValidatorsData)),
        # The sealing lottery ticket accumulator (𝛾_a).
        ('gamma_a', n(TicketsAccumulator)),
        # The sealing-key sequence of the current epoch (𝛾_s).
        ('gamma_s', n(TicketsOrKeys)),
        # The Bandersnatch ring commitment for the current epoch's ticket submissions (𝛾_z).
        ('gamma_z', n(BandersnatchRingCommitment)),
        # Posterior offenders sequence (ψ_o').
        ('post_offenders', 'Vec<Ed25519Public>'),
    ]

class SafroleInput(Struct):
    type_mapping = [
        # Timeslot index as found in the block's header (H_t).
        ('slot', n(TimeSlot)),
        # Per-block entropy generated from H_v.
        ('entropy', n(Entropy)),
        # Tickets extrinsic (E_T).
        ('extrinsic', n(TicketsXt)),
    ]

class OutputMarks(Struct):
    type_mapping = [
        # Epoch marker (H_e)
        ('epoch_mark', 'Option<EpochMark>'),
        # Tickets marker (H_w)
        ('tickets_mark', 'Option<TicketsMark>')
    ]

class SafroleOutput(Enum):
    type_mapping = {
        0: ('ok', n(OutputMarks)),
        1: ('err', n(Errno))
    }

class SafroleTestVector(StfTestVector):
    state_class = n(SafroleState)
    input_class = n(SafroleInput)
    output_class = n(SafroleOutput)
    errno_map = {
        0: "bad_slot",
        1: "unexpected_ticket",
        2: "bad_ticket_order",
        3: "bad_ticket_proof",
        4: "bad_ticket_attempt",
        5: "reserved",
        6: "duplicate_ticket"
    }
