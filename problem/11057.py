count = 0
breadth = int(input())

stack = []
for i in range(10):
    stack.append((1,i))

while stack:
    node = stack.pop()
    if node[0] <= breadth:
        for i in range(node[1],9):
            stack.append((node[0]+1, i))
        count += 1

print(count%10007)