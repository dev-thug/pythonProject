import sys

sys.setrecursionlimit(10 ** 6)
N, M = list(map(int, input().split()))

input = sys.stdin.readline

# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 이 조건 때문에 인접행렬로 그래프 구성
connected = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(M):
    x, y = list(map(int, input().split()))
    connected[x][y] = connected[y][x] = True


def dfs(root):
    for i in range(1, N + 1):
        if connected[root][i] and not visited[i]:
            visited[i] = True
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
