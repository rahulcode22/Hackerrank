#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
e=100
for i in range(k,n+1,k):
    if i<n:
        
        if c[i]==0:
            e=e-1
        else:
            e=e-3
    elif i==n:
        if c[i%n]==0:
            e=e-1
        else:
            e=e-3
        
print e
