n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

m = 0
a.sort()
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        adiff = abs(max(a[i:j])-min(a[i:j]))
        if 1 >= adiff >=0 and len(a[i:j]) > m:  
            m = len(a[i:j])       
print m
