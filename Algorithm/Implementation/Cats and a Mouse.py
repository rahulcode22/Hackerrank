#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    d1=abs(x-z)
    d2=abs(y-z)
    if d1>d2:
        print "Cat B"
    elif d1<d2:
        print "Cat A"
    else:
        print "Mouse C"
