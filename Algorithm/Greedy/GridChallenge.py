T = int(input())

all_grids = []
for t in range(T):
    N = int(input())
    n = [''.join(sorted(input().strip())) for i in range(N)]
    all_grids.append([N, n])

def check_condition(grid):
    answer = 'YES'
    for i in range(grid[0] - 1):
        for j in range(grid[0]):
            if grid[1][i][j] > grid[1][i+1][j]:
                answer = 'NO'
                return answer
    return answer

answers = []

for grid in all_grids:
    answers.append(check_condition(grid))

print('\n'.join(answers))
