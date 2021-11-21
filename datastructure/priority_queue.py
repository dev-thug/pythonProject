# 우선순위 큐 Priority Queue (Heap)
# 내부적으로 이진트리형태의 힙으로 작동
# 삽입/삭제 : O(logN)
# 파이썬에서는 min-heap

# from queue import PriorityQueue # thread-safe 하여 속도가 느린다

import heapq as hp# thread-safe 하지않아 속도가 빠르다

pq = []
hp.heappush(pq, 456)
hp.heappush(pq, 123)
hp.heappush(pq, 789)

print(f"size : {len(pq)}")

while len(pq) > 0:
    print(hp.heappop(pq))
