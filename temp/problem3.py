import sys


def solution(n):

    if n % 5 == 0:
        return n // 5
    elif n % 3 == 0:
        return n // 3

    q = n//5
    while q>0:
        mod = n-5*q
        if mod%3 == 0 :
            return q+mod//3
        q -= 1

    return -1


n = 22

print(solution(n))
