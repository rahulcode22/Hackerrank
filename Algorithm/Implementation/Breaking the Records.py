#!/bin/python

import sys


n = int(raw_input().strip())
score = map(int, raw_input().strip().split(' '))
# your code goes here
c,z=0,0
max=score[0]
min=score[0]
for i in range(1,n):
    if score[i]>max:
        max=score[i]
        c=c+1
    elif score[i]<min:
        min=score[i]
        z=z+1
    
print c,z
    
