#!/usr/bin/env python3

import hashlib
import json
import sys

## Graypaper conforming implementation of the trie merklization (Appendix D)
## Based on GP 0.2.2

# Blake2b-256
def hash(data):
    return hashlib.blake2b(data, digest_size=32).digest()

# GP (286)
def branch(l, r):
    assert len(l) == 32
    assert len(r) == 32
    head = l[0] & 0xfe
    return bytes([head]) + l[1:] + r

# GP (287)
def leaf(k, v):
    if len(v) <= 32:
        head = 0b01 | (len(v) << 2)
        return bytes([head]) + k[:-1] + v + ((32 - len(v)) * b'\0')
    head = 0b11
    return bytes([head]) + k[:-1] + hash(v)

def bit(k, i):
    return (k[i >> 3] & (1 << (i & 7))) != 0

# GP (289)
def merkle(kvs, i=0):
    if not kvs:
        return 32 * b'\0'
    if len(kvs) == 1:
        encoded = leaf(*kvs[0])
    else:
        l = []
        r = []
        for k, v in kvs:
            if bit(k, i):
                r.append((k, v))
            else:
                l.append((k, v))
        encoded = branch(merkle(l, i + 1), merkle(r, i + 1))
    assert len(encoded) == 64
    return hash(encoded)

## Random number generation

def wrap_64(x):
    return x & ((1 << 64) - 1)

def rol_64(x, y):
    return wrap_64(x << y) | (x >> (64 - y))

class Rng:
    '''Xoshiro256** RNG.

    Matches Xoshiro256StarStar in crates.io's rand_xoshiro 0.6.0 with rand 0.8.5.'''

    def __init__(self, seed):
        def split_mix_64():
            nonlocal seed
            seed = wrap_64(seed + 0x9e3779b97f4a7c15)
            res = wrap_64((seed ^ (seed >> 30)) * 0xbf58476d1ce4e5b9)
            res = wrap_64((res ^ (res >> 27)) * 0x94d049bb133111eb)
            return res ^ (res >> 31)

        self.__s = [split_mix_64() for i in range(4)]

    def next_64(self):
        res = wrap_64(rol_64(wrap_64(self.__s[1] * 5), 7) * 9)

        t = wrap_64(self.__s[1] << 17)

        self.__s[2] ^= self.__s[0]
        self.__s[3] ^= self.__s[1]
        self.__s[1] ^= self.__s[2]
        self.__s[0] ^= self.__s[3]

        self.__s[2] ^= t

        self.__s[3] = rol_64(self.__s[3], 45)

        return res

    def next_32(self):
        return self.next_64() >> 32

    def bytes(self, num):
        data = bytearray()
        while len(data) < num:
            if (num - len(data)) > 4:
                data.extend(self.next_64().to_bytes(8, byteorder='little'))
            else:
                data.extend(self.next_32().to_bytes(4, byteorder='little'))
        return bytes(data[:num])

    def range_64(self, low, high):
        assert 0 <= low <= high < (1 << 64)

        r = high - low + 1
        if r == (1 << 64):
            assert low == 0
            return self.next_64()

        zone = r << (64 - r.bit_length())
        while True:
            x = self.next_64() * r
            if wrap_64(x) < zone:
                return low + (x >> 64)

## Test vector generation

def random_key(rng):
    return rng.bytes(32)

def random_value(rng, size=None):
    if size is None:
        size = rng.range_64(0, 64)
    return rng.bytes(size)

def inputs():
    rng = Rng(42)

    yield []
    yield [(random_key(rng), b'')]
    yield [(random_key(rng), random_value(rng, 1))]
    yield [(random_key(rng), random_value(rng, 32))]
    yield [(random_key(rng), random_value(rng, 33))]
    yield [(random_key(rng), random_value(rng, 60))]

    k1 = random_key(rng)
    k2 = bytes([k1[0] ^ 1]) + k1[1:]
    yield [(k1, random_value(rng)), (k2, random_value(rng))]

    k1 = random_key(rng)
    k2 = k1[:1] + bytes([k1[1] ^ 1]) + k1[2:]
    yield [(k1, random_value(rng)), (k2, random_value(rng))]

    yield [(random_key(rng), random_value(rng)) for i in range(2)]
    yield [(random_key(rng), random_value(rng)) for i in range(5)]
    yield [(random_key(rng), random_value(rng)) for i in range(10)]

def hex(data):
    return ''.join(f'{x:02x}' for x in data)

def test_vectors():
    for kvs in inputs():
        yield {
            'input': {hex(k): hex(v) for k, v in kvs},
            'output': hex(merkle(kvs)),
        }

def main():
    json.dump(list(test_vectors()), sys.stdout, indent='    ')

main()
