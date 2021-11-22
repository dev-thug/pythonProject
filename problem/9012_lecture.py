for _ in range(int(input())):
    stack = []
    isVPS = True
    for ch in input():
        if ch == "(":
            stack.append(ch)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                isVPS = False
                break

    if stack: # == len(stack) > 0:
        isVPS = False

    print("YES" if isVPS else "NO")
