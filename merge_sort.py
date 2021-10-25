def mergesort(S):
    n = len(S)
    if n <= 1:
        return S
    else:
        mid = n // 2
        U = mergesort(S[0: mid])
        V = mergesort(S[mid: n])
        return merge(U, V)


def merge(U, V):
    S = []
    i = j = 0
    while i < len(U) and j < len(V):
        if U[i] < V[j]:
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j += 1

    if i < len(U):
        S += U[i: len(U)]
    else:
        S += V[j: len(V)]
    return S


def mergesort_enhanced(s, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort_enhanced(s, low, mid)
        mergesort_enhanced(s, mid + 1, high)
        merge_enhanced(s, low, mid, high)


def merge_enhanced(s, low, mid, high):
    result = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if s[i] < s[j]:
            result.append(s[i])
            i += 1
        else:
            result.append(s[j])
            j += 1
    if i <= mid:
        result += s[i: mid + 1]
    else:
        result += s[j: high + 1]
    for k in range(low, high + 1):
        s[k] = result[k - low]


if __name__ == '__main__':
    S = [4, 7, 9, 2, 1, 13, 8, 5, 6, 12]
    # print(S)
    # X = mergesort(S)
    # print(X)

    mergesort_enhanced(S, 0, len(S) - 1)
    print(S)
