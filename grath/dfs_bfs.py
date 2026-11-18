from collections import deque

def dfs_vis(graph, v, vis, par, res):
    vis[v] = True
    res.append(v)

    for i in range(len(graph)):
        if graph[v][i] == 1 and vis[i] == False:
            par[i] = v
            dfs_vis(graph, i, vis, par, res)


def dfs(graph, start):
    n = len(graph)

    vis = [False] * n
    par = [-1] * n
    res = []

    dfs_vis(graph, start, vis, par, res)

    return res, par

def bfs(graph, start):
    n = len(graph)

    vis = [False] * n
    par = [-1] * n
    res = []
    dis = [-1] * n

    queue = deque()
    queue.append(start)

    vis[start] = True
    dis[start] = 0

    while queue:
        v = queue.popleft()
        res.append(v)

        for i in range(len(graph)):
            if graph[v][i] == 1 and vis[i] == False:
                vis[i] = True

                dis[i] = dis[v] + 1

                par[i] = v

                queue.append(i)

    return res, dis, par


graph = [
    [0, 1, 0, 1,0 ,1],
    [1,0,1,0,0,0],
    [0,1,0,1,0,0],
    [1,0,1,0,1,0],
    [0,0,0,1,0,1],
    [1,0,0,0,1,0]
]

print(dfs(graph, 0))

print(bfs(graph, 0))

