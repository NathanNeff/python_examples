#!/usr/bin/env python
medium_ips='''
medium one
medium two
'''[1:-1]

small_ips='''
one
two
three
four
five
size
seven
eight
'''[1:-1]

small_ips_list = small_ips.split('\n')

for idx, ip in enumerate(medium_ips.split('\n')):
        print "\n\nStudent %d" % idx
        print "\tMedium:\n\t%s" % ip
        print

        print "\tSmall: "
        for _ in range(4):
                print "\t" + small_ips_list.pop(0)
