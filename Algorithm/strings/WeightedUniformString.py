import sys
def check():
    pcount=ord(s[0])-96
    l.append(pcount)
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            l.append(pcount+(ord(s[i])-96))
            pcount=pcount+(ord(s[i])-96)
        else:
            pcount=ord(s[i])-96
            l.append(pcount)
    l.sort(reverse=True)


l=[]
s = list(raw_input().strip())
check()
l=set(l)
n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())
    if x in l:
        print "Yes"
    else:
        print "No"
