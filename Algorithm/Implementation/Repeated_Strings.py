#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
a_on_s=s.count("a")
a_after=a_on_s*(n//len(s))
a_mod=s[:n%len(s)].count("a")
print (a_after+a_mod)
