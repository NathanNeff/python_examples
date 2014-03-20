#!/usr/bin/env python
import random
random.seed()
words = [line.strip() for line in open('/usr/share/dict/words')]
print words[1]

max = len(words) - 1
print words[max]
for i in range(1, 1000000):
    r = random.randint(0, max)
    print words[r]
