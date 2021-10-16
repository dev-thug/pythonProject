def seqsearch(n, S, x):
    location = 0
    while location < n and S[location] != x:
        location += 1
    if location > n:
        location = -1
    return location


def sum(n, S):
    result = 0
    for i in range(0, n):
        result = result + S[i]
    return result


def exchage(S):
    n = len(S)
    for i in range(n-1):
        for j in range(i+1, n):
            if(S[i] > S[j]):
                S[i], S[j] = S[j], S[i] # swap

def matrixmult(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

    return C




if __name__ == '__main__':
    # S = [10, 7, 11, 5, 13, 8]

    A = [[2,3],
         [4,1]]

    B = [[5,7],
         [6,8]]

    print(f"A = {A}")
    print(f"B = {B}")
    C = matrixmult(A,B)
    print(f"C = {C}")
