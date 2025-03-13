import json
import os
import requests
from typing import Tuple

from gen_block import create_dummy_block
from spec_config import gen_flags

def fetch_vectors(spec: str):
    # Read the vestors from ./{spec}/{vector_name}.json
    result = []
    for file in os.listdir(f"./{spec}"):
        if file.endswith(".json"):
            with open(f"./{spec}/{file}", "r") as f:
                data = json.load(f)
                result.append((file, data))
    return result

def transform_block(input: dict) -> dict:
    block = create_dummy_block()
    block["extrinsic"]["tickets"] = input["extrinsic"]
    block["header"]["slot"] = input["slot"]
    block["header"]["epoch_mark"]["entropy"] = input["entropy"]
    return block

def transform_state(state: dict) -> dict:
    state["gamma"] = {}
    if "gamma_k" in state:
        state["gamma"]["k"] = state["gamma_k"]
        del state["gamma_k"]
    if "gamma_z" in state:
        state["gamma"]["z"] = state["gamma_z"]
        del state["gamma_z"]
    if "gamma_s" in state:
        state["gamma"]["s"] = state["gamma_s"]
        del state["gamma_s"]
    if "gamma_a" in state:
        state["gamma"]["a"] = state["gamma_a"]
        del state["gamma_a"]
    return state

def transform(vector: dict) -> Tuple[dict, dict, dict]:
    # Block transform
    block = transform_block(vector["input"])
    pre_state = transform_state(vector["pre_state"])
    post_state = transform_state(vector["post_state"])
    return block, pre_state, post_state

if __name__ == "__main__":
    vectors = fetch_vectors("tiny")
    for (file, vector) in vectors:
        input, pre_state, post_state = transform(vector)
        response = requests.post("http://localhost:8000/api/v1/safrole/validate", json={"input": {"block": input, "state": pre_state}, "output": {"state": post_state}, "flags": gen_flags("tiny")})
        result = response.json()
        if result.status != "ok":
            print(f"Failed: {file}")
            break