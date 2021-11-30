# 큐 Queue
# 연결리스트로 큐 구현시 삽입/삭제 : O(1)
# deque == Double-Ended QUEue

from queue import Queue # thread-safe 기능이 포함되어 있어 실제 속도가 느리다
from collections import deque # thread-safe 하지 않기 때문에 속도가 빨라 알고리즘 풀이에 적합한 큐
dq = deque()
dq.append(123)
dq.append(456)
dq.append(789)

print(f"size : {len(dq)}")

while len(dq) > 0:
    print(dq.popleft())