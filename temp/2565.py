import sys

# input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b, abs(a - b)))

lines.sort(key=lambda x: x[2])

ans = 0

for line in lines:
    for i in range(len(lines)):
        if line[0] < lines[i][0] and line[1] > lines[i][1]:
            break
        else:
            ans += 1

print(len(lines) - ans)
