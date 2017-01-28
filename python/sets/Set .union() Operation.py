# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
E=set(map(int,raw_input().split()))
b=int(raw_input())
F=set(map(int,raw_input().split()))
a= E|F
print len(a)
