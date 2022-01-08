from itertools import combinations

v = []
for _ in range(9):
    v.append(int(input()))

for i in combinations(v, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break