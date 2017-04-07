# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
arr=raw_input()
up,count=0,0
for i in arr:
    if i=='U':
        up +=1
        if up==0:
            count +=1
    else:
        up -=1
print count
