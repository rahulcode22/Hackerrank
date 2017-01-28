# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=raw_input().split()
arr=map(int,raw_input().split())
A=set(map(int,raw_input().split()))
B=set(map(int,raw_input().split()))
h=0
for i in list(arr):
    if i in A:
          h=h+1
    elif i in B:
          h=h-1
    else:
          h=h+0
print h
