S=map(str,raw_input())
s=set(S)

if((len(S)%len(s)==0) or ((len(S)-1)%(len(s)-1)==0) or (len(S)%len(s)==1)):
    print "YES"
else:
    print "NO"
