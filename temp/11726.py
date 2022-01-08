import sys

MOD = 10_007

dp = [0] * 1001

n = int(input())

dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n])

# sys.setrecursionlimit(10 ** 6)
# cache = [0 for _ in range(1001)]
#
# def tile(n):
#     if not cache[n]:
#         cache[n] = cache[n - 1] + cache[n - 2]
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return tile(n - 1) + tile(n - 2)
#
#
# print(tile(10))
