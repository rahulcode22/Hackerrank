# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k=raw_input().split()
for i in xrange(1,int(k)+1):
    print "\n".join(["".join(i) for i in list(combinations(sorted(list(s)),i))])
