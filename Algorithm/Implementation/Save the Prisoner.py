for _ in range(int(raw_input())):
    n, m, s = (int(i) for i in raw_input().split())
    print ((m + s - 2) % n + 1)
