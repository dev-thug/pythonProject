from collections import deque

n = int(input())
dq = deque()
for i in range(n):
    dq.append(i)
command = True
while len(dq) > 1:
    if command:
        dq.popleft()
        command = False
    else:
        dq.append(dq.popleft())
        command = True

print(dq.pop()+1)