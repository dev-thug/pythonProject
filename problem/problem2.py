from itertools import permutations

def solution(v):
    answer = -1

    for per in permutations(v, len(v)):
        sum = 0
        for i in range((len(v)-1)):
            sum += abs(per[i]-per[i+1])

        if answer<sum:
            answer = sum
        sum = 0

    return answer

v = [20,8,10,1,4,15]

print(solution(v))

