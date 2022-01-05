N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

low = 0
high = max(budgets)
mid = (low + high) // 2
answer = 0


def is_possible(mid):
    return sum(min(budget, mid) for budget in budgets) <= M


while low <= high:
    if is_possible(mid):
        low = mid + 1
        answer = mid
    else:
        high = mid - 1

    mid = (low + high) // 2

print(answer)
