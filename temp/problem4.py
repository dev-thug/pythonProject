from collections import deque


def solution(K, user_scores):
    users = []
    answer = 0
    for i in user_scores:
        array = i.split()
        users.append((array[0], array[1]))

    print(users)

    return answer


K = 3
user_scores = ["alex111 100", "cheries2 200", "alex111 200", "cheries2 150", "coco 50", "coco 200"]#["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]

print(solution(K, user_scores))
