#!/usr/bin/env python3
# Yes, this is a Bad YAML Parser, but at this stage we are not in the
# venv and do not know what modules the user has available, so for
# maximum compatibility, we are just assuming a plain Python distribution.
import argparse
import re
import sys
import os

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--sources", action="store_true")
group.add_argument("--family", action="store_true")
args = parser.parse_args()

with open(os.path.join("sources", "config-Geist.yaml")) as config:
    data = config.read()

if args.family:
    m = re.search(r"(?m)^familyName: (.*)", data)
    if m:
        print(m[1])
        sys.exit(0)
    else:
        print("Could not determine family name from config file!")
        sys.exit(1)

toggle = False
sources = []
for line in data.splitlines():
    if re.match("^sources:", line):
        toggle = True
        continue
    if toggle:
        m = re.match(r"^\s*-\s*(.*)", line)
        if m:
            sources.append("sources/" + m[1])
        else:
            toggle = False
if sources:
    print(" ".join(sources))
    sys.exit(0)
else:
    print("Could not determine sources from config file!")
    sys.exit(1)
