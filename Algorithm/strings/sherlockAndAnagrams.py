T = int(input().strip())
for a0 in range(T):
    s = input().strip()
    anag = 0
    map = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            s1 = ''.join(sorted(s[j:j + i + 1]))
            map[s1] = map.get(s1, 0) + 1
    for key in map:
        anag += (map[key] - 1) * map[key] // 2
    print(anag)s
