from collections import deque

N = int(input())

# 선언과 동시에 넣기
dq = deque(range(1, N+1))
# for i in range(1, N+1):
#     dq.append(i)

# print(dq)
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
    # print(dq)

print(dq.pop())