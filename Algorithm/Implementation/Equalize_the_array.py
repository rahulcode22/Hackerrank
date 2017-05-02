from collections import Counter
n=int(raw_input())
arr=map(int,raw_input().split(' '))
print (len(arr)-arr.count(max(set(arr),key=arr.count)))
