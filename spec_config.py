spec_config = {
    "tiny": {
        "epoch_length": 12,
        "validator_count": 6,
    },
    "full": {
        "epoch_length": 600,
        "validator_count": 1023,
    },
}

def gen_flags(spec: str) -> int:
    return {
        "spec": spec,
        "epoch_length": spec_config[spec]["epoch_length"],
        "validator_count": spec_config[spec]["validator_count"],
    }
