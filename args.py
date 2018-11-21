#!/usr/bin/env python
import sys
if len(sys.argv) > 1:
    print(sys.argv[1])

if len(sys.argv) == 1:
    print(sys.argv[0])
    sys.exit(1)

for arg,idx in enumerate(sys.argv):
    print(("arg {}: {}".format(arg,idx)))


