import collections
raw_input()
S=list(map(int,raw_input().split()))
lis=list([item for item, count in collections.Counter(S).items() if count < 2])
print lis[0]
