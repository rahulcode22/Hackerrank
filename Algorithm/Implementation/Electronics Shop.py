#!/bin/python

import sys


s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int,raw_input().strip().split(' '))
pendrives = map(int,raw_input().strip().split(' '))
max=-999
flag=False
for i in keyboards:
    for j in pendrives:
        if i+j<=s:
            if i+j>max:
                max=i+j
                flag=True
if flag:
    print max
else:
    print "-1"
