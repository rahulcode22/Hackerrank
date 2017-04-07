
import sys


n = int(raw_input().strip())
scores = sorted(set(map(int,raw_input().strip().split(' '))),reverse=True)
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here
for s in alice:
    while bool(scores) and  s>=scores[-1]:
        scores.pop()
    print len(scores)+1
    
    
