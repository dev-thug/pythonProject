N, M = list(map(int, input().split()))

# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 이 조건 때문에 인접행렬로 그래프 구성
connected = [[False] * N for _ in range(N)]
visited = [False * N]
stack = []
for _ in range(M):
    x, y = list(map(int, input().split()))
    connected[x-1][y-1] = connected[y-1][x-1] = True

stack.append(0)






