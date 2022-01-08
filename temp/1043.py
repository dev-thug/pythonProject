N, M = list(map(int, input().split()))
r = list(map(int, input().split()))
_r = r[1:]
real = [False] * (N + 1)

for i in _r:
    real[i] = True

party = []
for _ in range(M):
    party.append(list(map(int, input().split())))

for i in party:
    for j in range(i[0]):
        for k in range(len(real)):
            if real[k] and i[j + 1] == k:
                for l in range(i[0]):
                    p = i[l+1]
                    # print(p)
                    real[p] = True

count = 0
for i in party:
    for j in range(i[0]):
        if real[i[j + 1]]:
            count +=1
            break;

print(M-count)