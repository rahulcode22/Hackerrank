# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,n=raw_input().split()
print "\n".join("".join(i)  for i in list(combinations_with_replacement(sorted(s),int(n))))
