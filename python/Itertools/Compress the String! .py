# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = map(int,raw_input())

for k,g in groupby(s):
    print (len(list(g)),k),
