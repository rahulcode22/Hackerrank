#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
sum=a+b+c+d+e
print sum-max(a,b,c,d,e),sum-min(a,b,c,d,e)
