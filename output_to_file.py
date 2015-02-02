#!/usr/bin/env python
filename = "foo.txt"
output = open(filename, 'w')

for i in range(1, 100):
    output.write("BOOM")

output.close()
print "I just output BOOM to", filename
