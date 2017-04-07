#!/bin/python

import sys

from collections import Counter
n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here
coun=Counter(list(types))
for letter,count in coun.most_common(1):
    s= [letter,count]
print s[0]

