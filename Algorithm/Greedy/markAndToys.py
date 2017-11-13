n , k = raw_input().split()
n, k = [int(n), int(k)]
arr = sorted(map(int,raw_input().split()))
c = 0
for i in arr:
    if i <= k:
        c += 1
        k -= i
    if i > k:
        break
    if k == 0:
        break

print c
