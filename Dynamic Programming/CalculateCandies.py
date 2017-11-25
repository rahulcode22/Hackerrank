def calculateCandies(arr):
    n = len(arr)
    left = [0]*n
    right = [0]*n
    candies = 0
    left[0] = 1
    right[n-1] = 1
    for i in range(1,n):
        left[i] = left[i-1] + 1 if arr[i]> arr[i-1] else 1

    for i in range(n-2,-1,-1):
        right[i] = right[i+1] + 1 if arr[i] > arr[i+1] else 1

    for i in range(n):
        candies += max(left[i],right[i])

    return candies

n = int(raw_input())
lis = []
for i in range(n):
    lis.append(int(raw_input()))

print calculateCandies(lis)
