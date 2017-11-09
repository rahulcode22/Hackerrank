def lcs(x, y):
    dp = [[0]*(len(y)+1) for i in xrange(len(x)+1)]
    for i in xrange(len(x)+1):
        for j in xrange(len(y)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]

    return dp[len(x)][len(y)]

x, y = raw_input(), raw_input()
print lcs(x, y)
