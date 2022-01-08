# 내가 푼 풀이
n = int(input())

for i in range(n):
    s = input()
    stack = []
    flag = True
    for j in range(len(s)):
        if s[j] == "(":
            stack.append(s[i])
        elif s[j] == ")":
            if len(stack) == 0:
                flag = False
                break
            stack.pop()

    if len(stack) > 0:
        flag = False

    if flag is True:
        print("YES")
    else:
        print("NO")