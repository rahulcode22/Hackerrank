# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, k = raw_input().split()
print "\n".join(["".join(i) for i in list(permutations(sorted(list(s)),int(k)))])
