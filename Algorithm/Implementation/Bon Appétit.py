# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=raw_input().strip().split(' ')
n,k=[int(n),int(k)]
arr=map(int,raw_input().split(' '))
bcharged=int(raw_input())
s=arr.pop(k)
bactual=sum(arr)//2
if bactual==bcharged:
    print "Bon Appetit"
else:
    print bcharged-bactual
