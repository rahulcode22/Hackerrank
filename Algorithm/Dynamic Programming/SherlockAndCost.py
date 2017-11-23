
def get_max_cost(b):
    n = len(b)
    hi, low = 0, 0
    for i in range(1,n):
        high_to_low_diff = abs(b[i-1] - 1)
        low_to_high_diff = abs(b[i] - 1)
        high_to_high_diff = abs(b[i] - b[i-1])

        low_next = max(low, hi + high_to_low_diff)
        hi_next = max(hi+high_to_high_diff, low+low_to_high_diff)

        low = low_next
        hi = hi_next
    return max(hi, low)

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    arr = map(int,raw_input().split())
    print get_max_cost(arr)
