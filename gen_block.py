import random

from spec_config import spec_config


def create_dummy_bytes(size: int) -> bytes:
    """Create dummy bytes"""
    return '0x' + bytes(random.randint(0, 255) for _ in range(size)).hex()


def create_dummy_bytes32() -> bytes:
    """Create dummy bytes32"""
    return create_dummy_bytes(32)

def create_dummy_package_spec() -> dict:
    """Create dummy package spec"""
    return {
        "hash": create_dummy_bytes32(),
        "length": 42,
        "erasure_root": create_dummy_bytes32(),
        "exports_root": create_dummy_bytes32(),
        "exports_count": 69,
    }


def create_dummy_work_context() -> dict:
    """Create dummy work context"""
    return {
        "anchor": create_dummy_bytes32(),
        "state_root": create_dummy_bytes32(),
        "beefy_root": create_dummy_bytes32(),
        "lookup_anchor": create_dummy_bytes32(),
        "lookup_anchor_slot": 33,
        "prerequisites": [],
    }


def create_dummy_work_result() -> dict:
    """Create dummy work result"""
    return {
        "service_id": 16909060,
        "code_hash": create_dummy_bytes32(),
        "payload_hash": create_dummy_bytes32(),
        "accumulate_gas": 42,
        "result": {"ok": create_dummy_bytes(16)},
    }


def create_dummy_work_report() -> dict:
    """Create dummy work report"""
    return {
        "package_spec": create_dummy_package_spec(),
        "context": create_dummy_work_context(),
        "core_index": 3,
        "authorizer_hash": create_dummy_bytes32(),
        "auth_output": "0x0102030405",
        "segment_root_lookup": [],
        "results": [create_dummy_work_result()],
    }


def create_dummy_validator_signatures() -> list[dict]:
    """Create dummy validator signatures"""
    return [
        {
            "validator_index": i,
            "signature": create_dummy_bytes(64),
        }
        for i in range(2)
    ]


def create_dummy_tickets() -> list[dict]:
    """Create dummy tickets"""
    return [
        {
            "attempt": i,
            "signature": create_dummy_bytes(784),
        }
        for i in range(3)
    ]


def create_dummy_preimages() -> list[dict]:
    """Create dummy preimages"""
    return [
        {
            "requester": 16909060 + i,
            "blob": create_dummy_bytes32(),
        }
        for i in range(3)
    ]


def create_dummy_guarantees() -> list[dict]:
    """Create dummy guarantees"""
    return [
        {
            "report": create_dummy_work_report(),
            "slot": 42,
            "signatures": create_dummy_validator_signatures(),
        }
        for i in range(3)
    ]


def create_dummy_assurances() -> list[dict]:
    """Create dummy assurances"""
    return [
        {
            "anchor": create_dummy_bytes32(),
            "bitfield": "0x01",
            "validator_index": i,
            "signature": create_dummy_bytes(64),
        }
        for i in range(2)
    ]


def create_dummy_judgements() -> list[dict]:
    """Create dummy judgements"""
    return [
        {
            "vote": True,
            "index": i,
            "signature": create_dummy_bytes(64),
        }
        for i in range(5)
    ]


def create_dummy_verdicts() -> list[dict]:
    """Create dummy verdicts"""
    return [
        {
            "target": create_dummy_bytes32(),
            "age": 3,
            "votes": create_dummy_judgements(),
        }
    ]


def create_dummy_culprits() -> list[dict]:
    """Create dummy culprits"""
    return [
        {
            "target": create_dummy_bytes32(),
            "key": create_dummy_bytes32(),
            "signature": create_dummy_bytes(64),
        }
    ]


def create_dummy_faults() -> list[dict]:
    """Create dummy faults"""
    return [
        {
            "target": create_dummy_bytes32(),
            "vote": False,
            "key": create_dummy_bytes32(),
            "signature": create_dummy_bytes(64),
        }
    ]


def create_dummy_disputes() -> dict:
    """Create dummy disputes"""
    return {
        "verdicts": create_dummy_verdicts(),
        "culprits": create_dummy_culprits(),
        "faults": create_dummy_faults(),
    }


def create_dummy_extrinsics() -> dict:
    """Create dummy extrinsics"""
    return {
        "tickets": create_dummy_tickets(),
        "preimages": create_dummy_preimages(),
        "guarantees": create_dummy_guarantees(),
        "assurances": create_dummy_assurances(),
        "disputes": create_dummy_disputes(),
    }


def create_dummy_header(spec: str = "tiny") -> dict:
    """Create dummy header"""
    return {
        "parent": create_dummy_bytes32(),
        "parent_state_root": create_dummy_bytes32(),
        "extrinsic_hash": create_dummy_bytes32(),
        "slot": 0,
        "epoch_mark": {
            "entropy": create_dummy_bytes32(),
            "tickets_entropy": create_dummy_bytes32(),
            "validators": [create_dummy_bytes32() for _ in range(spec_config[spec]["validator_count"])],
        },
        "tickets_mark": [
            {
                "id": create_dummy_bytes32(),
                "attempt": 0,
            }
            for i in range(spec_config[spec]["epoch_length"])
        ],
        "offenders_mark": [],
        "entropy_source": create_dummy_bytes(96),
        "author_index": 0,
        "seal": create_dummy_bytes(96),
    }


def create_dummy_block(spec: str = "tiny") -> dict:
    return {
        "header": create_dummy_header(spec),
        "extrinsic": create_dummy_extrinsics(),
    }