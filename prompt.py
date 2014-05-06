#!/usr/bin/env python
while True:
    reply = raw_input("type something ")
    if reply.lower() == "something": 
        print "Good job"
        break
    else: 
        print "Bad monkey.  " + reply

