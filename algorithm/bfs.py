adjacent = [[0] * 13 for _ in range(13)]
adjacent[0][1] = adjacent[0][7] = 1
adjacent[1][2] = adjacent[1][5] = 1

def dfs(now):
    for i in range(13):
        if adjacent[now][i]:
            dfs(i)


dfs(0)