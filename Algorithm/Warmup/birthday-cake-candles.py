#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
s=max(height)
print height.count(s)
