import sys
from itertools import combinations

N, M = list(map(int, input().split()))

city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

chicken_open = combinations(chicken, M)

result = []

for i in chicken_open:
    _sum = 0
    for j in house:
        dist = sys.maxsize
        for k in i:
            if abs(j[0]-k[0])+abs(j[1]-k[1])< dist:
                dist = abs(j[0]-k[0])+abs(j[1]-k[1])
        _sum += dist

    result.append(_sum)


result.sort()

print(result[0])



# chickens = []
#
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 2:
#             chickens.append((i, j))
#
# open_chickens = []
#
# for i in combinations(chickens, M):
#     open_chickens.append(i)
#
# # 뽑힌 조합의 갯수만큼 최솟값이 나오게 됨
# result = 0
#
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 1:
#             dist = sys.maxsize
#             for chicken in open_chickens:
# #                 # if 걸엇 집(i,j) 뽑아낸 치킨집과의 치킨 거리 최솟값 저장
#                 for k in chicken:
#                     if dist > (abs(i-k[0])+abs(j-k[1])):
#                         dist = (abs(i-k[0])+abs(j-k[1]))
# #                 result += dist
#             result += dist
#
# print(result)
#
#
# # for i in open_chickens:
# #     for j in i:
# #         for k in range(N):
# #             for l in range(N):
# #                 city[]
