#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    # your code goes here
    if grade<38:
        print grade
    elif grade%5<3:
        print grade
    
    else:
        num=((grade//5)+1)*5
        print num
