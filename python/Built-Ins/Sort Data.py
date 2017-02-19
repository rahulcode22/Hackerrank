n, m = map(int, input().split())
nums = [list(map(int, input().split())) for i in range(n)]
k = int(input())

nums.sort(key=lambda x: x[k])

for line in nums:
    print(*line, sep=' ')
