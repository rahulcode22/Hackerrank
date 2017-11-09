# Enter your code here. Read input from STDIN. Print output to STDOUT
t= int(raw_input())
for i in range(t):
    s=raw_input()
    n=len(s)
    c=0
    for i in range(n//2):
        j=n-i-1
        if s[i]!=s[j]:
            c=c+abs(ord(s[i])-ord(s[j]))
    print c
