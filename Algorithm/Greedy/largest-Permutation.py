n,k = map(int,raw_input().split())
arr = map(int,raw_input().split())
brr = [0 for _ in range(n+1)]
for i in range(n):
    brr[arr[i]] = i
for i in range(n):
    if k == 0:
        break
    if arr[i] == n-i:
        continue
    else:
        ind = brr[n-i]
        arr[i],arr[ind] = arr[ind],arr[i]
        brr[arr[i]],brr[arr[ind]] = brr[arr[ind]],brr[arr[i]]
    k -=1
print " ".join(map(str,arr))
