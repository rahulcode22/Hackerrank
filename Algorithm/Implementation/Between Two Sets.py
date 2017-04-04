#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
lis=[x for x in range(max(a),min(b)+1) if sum(i%x for i in b)==0 and sum(x%i for i in a)==0]
print len(lis)
