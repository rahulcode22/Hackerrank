n, x = map(int, raw_input().split())
all_scores = [map(float, raw_input().split()) for _ in range(x)]

for student, score in zip(range(1, n+1), zip(*all_scores)):
    print sum(score)/x
