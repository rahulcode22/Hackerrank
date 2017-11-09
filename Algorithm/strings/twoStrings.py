# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
n = int(n)
for i in range(0, n):
    s1 = set(raw_input())
    s2 = set(raw_input())
    result = s1.intersection(s2)
    if not result:
        print 'NO'
    else:
        print 'YES'
