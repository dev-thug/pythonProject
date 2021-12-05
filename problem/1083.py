
N = int(input())
A = list(map(int, input().split()))
S = int(input())
index = 0
for i in range(S):
    if S > N:
        count = -1
    else:
        count = S-i
    if max(A[index:count]) == A[index]:
        index += 1

    # for i in range(N-2):
    #     if A[i]<A[i+1]:
    #         A[i], A[i+1] = A[i+1], A[i]
    #         break

print(A)

# 5
# 4 1 3 5 2 7
# 2

# 4 3 1 5 2 7

# 4 5 1 3 2 7




# 3 1 5 4 2  / 5
# 3 5 1 4 2 / 4
# 5 3 1 4 2 / 3
# 5 3 4 1 2 / 2
# 5 4 3 1 2 / 1
# 5 4 3 2 1

# 3 4 3 1 5