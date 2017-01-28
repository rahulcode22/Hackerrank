int(raw_input())
a=set(map(int,raw_input().split()))
int(raw_input())
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
d=sorted(c)
for i in (list(d)):
    print i
