from collections import Counter
for _ in range(int(input())):
    s = input()
    l = len(s)
    if l % 2 == 1:
        print(-1)
    else:
        count = 0
        s1, s2 = Counter(s[:l//2]), Counter(s[l//2:])
        for char in s2:
            current = s2[char] - s1.get(char,0)
            if current > 0:
                count += current
        print(count)
