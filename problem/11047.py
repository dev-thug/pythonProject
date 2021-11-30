N, K = map(int, input().split(" "))

coins = [int(input()) for _ in range(N)]
coins.reverse()
result = 0

for coin in coins:
    result += K // coin  # 몫 구하는 연산
    K %= coin  # 나머지 연산

print(result)
