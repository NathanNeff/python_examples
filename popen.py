#!/usr/bin/env python
import os
import sys
from os import popen

cmd  = "cat ./README.md"
w, r = os.popen2(cmd)
got = r.read()
print "I got \"" + got + "\""
