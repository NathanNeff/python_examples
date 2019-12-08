#!/usr/bin/env python3
# TODO Read a file from STDIN and print random lines
import fileinput
import sys
import random
pct = 10
if len(sys.argv) > 1:
    pct = int(sys.argv[1])

for line in fileinput.input():
    if random.randint(1,100) < pct:
        print(line, end='')
