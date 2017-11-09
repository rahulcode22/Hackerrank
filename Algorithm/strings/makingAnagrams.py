# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
a=Counter(raw_input())
b=Counter(raw_input())
print sum((a-b).values() +(b-a).values())
