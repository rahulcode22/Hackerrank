n = int(raw_input())
arr = map(int,raw_input().split())
arr = sorted(arr, reverse = True)
res = 0
for i in range(n):
    res += arr[i]*(2**i)
print res
