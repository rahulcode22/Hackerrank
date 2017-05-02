n, m= map(int, input().split())
s= [input() for _ in range(n)]
mx=[]
for i in range(n):
    for j in range(n):
        if i!=j:    mx.append(bin(int(s[i], 2)| int(s[j], 2))[2:].count('1'))
print(max(mx), mx.count(max(mx))//2, sep='\n')
