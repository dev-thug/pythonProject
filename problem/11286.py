import heapq as hp
import sys
pq = []

input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x:
        hp.heappush(pq, (abs(x), x))
    else:
        if pq:
            print(hp.heappop(pq)[1])
        else:
            print(0)