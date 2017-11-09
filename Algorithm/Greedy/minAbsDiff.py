n = int(raw_input())
arr = map(int,raw_input().split())
arr.sort()
minOfList = arr[len(arr)-1]
for i in range(len(arr)-1):
    if abs(arr[i] - arr[i-1]) <= minOfList:
        minOfList = abs(arr[i]-arr[i-1])
print minOfList
