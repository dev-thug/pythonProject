# 우선순위 큐 Priority Queue (Heap)
# 내부적으로 이진트리형태의 힙으로 작동
# 삽입/삭제 : O(logN)
# 파이썬에서는 min-heap

import heapq

pq = []
heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)

print(f"size : {len(pq)}")

while len(pq) > 0:
    print(heapq.heappop(pq))
