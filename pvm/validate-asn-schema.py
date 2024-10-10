#!/usr/bin/env python3

from pathlib import Path
import asn1tools

schema = asn1tools.compile_files("schema.asn", codec="jer")

for path in Path("programs").iterdir():
    print(path)
    schema.encode("Testcase", schema.decode("Testcase", open(path, "rb").read()))
