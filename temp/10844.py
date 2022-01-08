n = int(input())

MOD = 1_000_000_000

dp = [[1] * 10 for _ in range(n)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
#
# for i in dp:
#     print(i[1:])

print(sum(dp[n-1][1:]) % MOD)
