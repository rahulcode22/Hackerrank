#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    s = raw_input().strip()
    s=set(s)
    print len(s)
