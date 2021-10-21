def binary_search(n, S, x):
    low = 0
    high = n
    location = -1
    while low <= high and location == -1:
        mid = (low + high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return location


def binary_search_recursive(S, low, high, target):
    if low > high:
        return 0
    else:
        mid = (low + high) // 2
        if target == S[mid]:
            return mid
        elif target < S[mid]:
            return binary_search_recursive(S, low, mid - 1, target)
        else:
            return binary_search_recursive(S, mid + 1, high, target)


if __name__ == '__main__':
    S = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]
    x = 18
    print(binary_search_recursive(S, 0, len(S), x))
