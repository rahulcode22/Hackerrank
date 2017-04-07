#!/bin/python

import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
# your code goes here
print min(p//2,n//2-p//2)
