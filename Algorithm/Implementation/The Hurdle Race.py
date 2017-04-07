
import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here
if k>= max(height):
    print "0"
else:
    print abs(k-max(height))
