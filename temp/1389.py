import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dq = deque()
adj = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = True

answer = sys.maxsize
min_index = 0
print(adj)


def bfs(root):
    answers = [0] * (N + 1)
    visited = [False] * (N + 1)
    dq.append(root)
    visited[root] = True
    while len(dq) > 0:
        idx = dq.popleft()
        for i in range(1, N + 1):
            if adj[idx][i] and not visited[i]:
                answers[i] = answers[idx] + 1
                visited[i] = True
                dq.append(i)
    return sum(answers)


for i in range(1, N + 1):
    total = bfs(i)
    if total < answer:
        answer = total
        min_index = i

print(min_index)

# def bfs(root):
#     dq.append(root)
#     while len(dq) > 0:
#         root = dq.popleft()
#         for i in range(N + 1):
#             if adj[root][i]:
#                 dq.popleft()
#                 answers[root] += 1
#             dq.append(i)
