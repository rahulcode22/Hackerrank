#!/bin/python

def issubstr(substr,mystr,start_index):
	for i in substr:
		start_index=mystr.find(i,start_index)+1
		if start_index==0:
			return False
	return True

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    start_index=0
    # your code goes here
    substr="hackerrank"
    if issubstr(substr,s,start_index):
        print "YES"
    else:
        print "NO"
   
