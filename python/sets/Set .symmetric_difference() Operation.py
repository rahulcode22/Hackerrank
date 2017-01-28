raw_input()
E=set(map(int,raw_input().split()))
raw_input()
F=set(map(int,raw_input().split()))
res=E^F
print len(res)
