N, L = map(int, input().split())
waters = list(map(int, input().split()))
waters.sort()
cnt = 0
tape = 0
for water in waters:
    if water>tape:
        tape = water+L-1
        cnt += 1

print(cnt)