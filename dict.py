#!/usr/bin/env python
words = {}
if 'foo' in words:
    words['foo'] = words['foo'] + 1
else:
    words['foo'] = 1

print words

if 'foo' in words:
    words['foo'] = words['foo'] + 1
else:
    words['foo'] = 1

print words

words['bar'] = 3

print words

sumz = 0
for k in words.keys():
    sumz += words[k]

foos = words['foo']
bars = words['bar']

print sumz

print foos, "divided by", sumz, "is:", float(foos)/sumz

print bars, "divided by", sumz, "is:", float(bars)/sumz



