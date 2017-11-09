#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
number = raw_input().strip()
flag=True
c=0
lis=list(number)
for i in range(n):
    if lis[i] !=lis[n-i-1]:
        c=c+1
        if lis[i]>lis[n-i-1]:
            lis[n-i-1]=lis[i]
        else:
            lis[i]=lis[n-i-1]
        if c>k:
            flag=False
if flag:
    print ''.join(lis)
else:
    print "-1"

    s
