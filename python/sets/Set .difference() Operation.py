# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
E=set(map(int,raw_input().split()))
raw_input()
F=set(map(int,raw_input().split()))
a=E-F
print len(a)
