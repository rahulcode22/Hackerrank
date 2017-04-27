# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
arr=map(int,raw_input().split(' '))
for x in range(1,n+1):
    for i in range(len(arr)):
        if x==arr[i]:
            j=arr.index(i+1)
            print j+1
