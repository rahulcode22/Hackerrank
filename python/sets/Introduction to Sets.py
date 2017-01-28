# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
s=set(map(int,raw_input().split()))
print(sum(s)/float(len(s)))
