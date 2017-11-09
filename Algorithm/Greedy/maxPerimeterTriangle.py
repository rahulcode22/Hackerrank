n = int(raw_input())
lenArr = sorted(map(int,raw_input().split()))

i = n-3
while i >= 0 and (lenArr[i] + lenArr[i+1] <= lenArr[i+2]):
    i -= 1
if i >= 0:
    print lenArr[i],lenArr[i+1],lenArr[i+2]
else:
    print "-1"
