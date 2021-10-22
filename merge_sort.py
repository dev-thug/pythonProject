def mergesort(S):
    n = len(S)
    if n <= 1:
        return S
    else:
        mid = n // 2
        U = mergesort(S[0 : mid])
        V = mergesort(S[mid : n])
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
        S += U[i : len(U)]
    else:
        S += V[j : len(V)]
    return S

if __name__ == '__main__':
    S = [27, 10, 12, 20, 25, 13, 15, 22]
    print(S)
    X = mergesort(S)
    print(X)