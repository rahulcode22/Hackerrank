#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
lis=[ord(char)-96 for char in word]
width=len(word)
max=-999
for i in lis:
    if h[i-1]>max:
        max=h[i-1]
print width*max
