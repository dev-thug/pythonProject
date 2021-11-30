n = int(input())

result = 0
rgb = []

# for i in range(n):
#     costs = list(map(int, input().split(" ")))
#     if i == 0:
#         cost = min(costs)
#         rgb.append(costs.index(cost))

for i in range(n):
    costs = list(map(int, input().split(" ")))
    if i == 0:
        cost = min(costs)
        rgb[i] = costs.index(cost)
        result += cost
    elif i > 2:

        temp = costs.copy()
        dx = temp[rgb[i - 1]]
        dy = temp[rgb[i - 2]]
        temp.remove(dx)
        temp.remove(dy)
        cost = temp.pop()
        print(cost)
        rgb[i] = costs.index(cost)
        result += cost
    else:

        temp = costs.copy()
        temp.pop(rgb)
        cost = min(temp)
        print(cost)
        rgb[i] = costs.index(cost)
        result += cost

print(result)
