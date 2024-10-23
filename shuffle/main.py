#!/usr/bin/env python3

import hashlib
import json
import sys

def hash(data):
    return hashlib.blake2b(data, digest_size=32).digest()

def hex(data):
    return ''.join(f'{x:02x}' for x in data)

def compute_shuffle_eq329(s, r):
    if len(s) > 0:
        l = len(s)
        index = r[0] % l
        head = s[index]

        s_post = s.copy()
        s_post[index] = s[l-1]

        return [head] + compute_shuffle_eq329(s_post[:-1], r[1:])
    else:
        return []

def number_vector(n): 
    return [x for x in range(n)]

def default_seed():
    return [i for i in range(32)]

def inputs_Eq331():
    seed = default_seed()

    yield(number_vector(0), seed)
    yield(number_vector(8), seed)
    yield(number_vector(16), seed)
    yield(number_vector(20), seed)

    yield(number_vector(50), seed)
    yield(number_vector(100), seed)
    yield(number_vector(200), seed)
    yield(number_vector(341), seed)


def to_le_bytes(n, k):
    return n.to_bytes(k, 'little')

def from_le_bytes(b):
    return int.from_bytes(b, 'little')

def compute_q(h, l):
    result = []
    for i in range(l):  
        preimage = bytes(h.copy()) + to_le_bytes(i // 8, 4)
        offset = 4*i % 32
        slice = hash(preimage)[offset:offset + 4] 
        result.append(from_le_bytes(slice))

    return result

def compute_shuffle_eq331(s, h):
    l = len(s)
    r = compute_q(h, l)

    return compute_shuffle_eq329(s, r)

def is_permutation(list1, list2):
    return set(list1) == set(list2)

def test_vectors_eq331():
    for term in inputs_Eq331():
        s, r = term
        output = compute_shuffle_eq331(s, r)
        assert(is_permutation(s, output))

        yield {
            'input': len(s),
            'entropy': hex(r),
            'output': output,
        }

def main():
    json.dump(list(test_vectors_eq331()), sys.stdout, indent='    ')

main()
