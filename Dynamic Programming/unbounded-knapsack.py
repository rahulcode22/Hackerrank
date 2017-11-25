#Tricky one..Learnt a new concept
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(15000)
def modifiedKnapsack(arr,k,n):
    if n == 0 or k == 0:
        return 0
    if arr[n-1] > k:
        return modifiedKnapsack(arr,k,n-1)
    return max(arr[n-1] + modifiedKnapsack(arr,k-arr[n-1],n),modifiedKnapsack(arr,k,n-1))
t = int(raw_input())
for i in range(t):
    n, k = raw_input().split()
    n, k = [int(n), int(k)]
    arr = map(int,raw_input().split())
    print modifiedKnapsack(arr,k,n)
