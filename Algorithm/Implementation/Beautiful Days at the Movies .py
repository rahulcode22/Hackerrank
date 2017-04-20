# Enter your code here. Read input from STDIN. Print output to STDOUT
i,j,k=map(int,raw_input().strip().split(' '))
c=0
for a in range(i,j+1):
    rev=''.join(reversed(str(a)))
    if abs(a-int(rev))%k==0:
        c=c+1
print c
        
