#!/bin/python

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
if y1-y2>=1:
    print "10000"
elif m1-m2>=1:
    print 500*(m1-m2)
else:
    print 15*(d1-d2)
