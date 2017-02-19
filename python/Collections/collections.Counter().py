from collections import Counter
raw_input()
S=Counter(map(int,raw_input().split()))
x=raw_input()
total=[]
for i in range(int(x)):
    a, b=map(int,raw_input().split())
    if(S[a]>0):
        total.append(b)
        S.subtract(Counter([a]))
print sum(total)
