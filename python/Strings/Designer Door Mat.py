N, M = map(int,raw_input().split()) 
for i in range(1,N,2): 
    print ((i*".|.").center(M,"-"))
print ("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print ((i*".|.").center(M,"-"))
