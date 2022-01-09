import sys

n = int(input())


def solution(n):
    for _ in range(n):
        input = sys.stdin.readline

        N = int(input())

        scores = []
        for _ in range(N):
            a, b = map(int, input().split())
            scores.append((a, b))

        scores.sort(key=lambda x: x[0])

        ans = 1
        index = scores[0][1]
        for score in scores:
            if score[1] < index:
                index = score[1]
                ans += 1

        print(ans)


solution(n)
