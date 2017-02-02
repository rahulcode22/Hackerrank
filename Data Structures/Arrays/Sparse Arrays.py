from collections import Counter
c = Counter()
for i in range(int(input())):
    c[input()] += 1
for i in range(int(input())):
    print(c[input()])
