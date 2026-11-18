def dijkstra(grath, start):
    n = len(grath)
    visited = [False] *  n
    dist = [None] * n
    prev = [None] * n

    dist[start] = 0

    for i in range(n):
        tmp = None

        for j in range(n):
            if not visited[j] and dist[j] is not None:
                if tmp is None or dist[j] < dist[tmp]:
                    tmp = j

        if tmp is None:
            break

        visited[tmp] = True

        for k in range(n):
            if grath[tmp][k] is None or visited[k]:
                continue

            dist_val = dist[tmp] + grath[tmp][k]

            if dist[k] is None or dist_val < dist[k]:
                dist[k] = dist_val
                prev[k] = tmp

    return dist, prev



grath = [
    [None, 3, 1, 3, None, None],
    [3, None, 4, None, None, None],
    [1, 4, None, None, 7, 5],
    [3, None, None,None, None, 2],
    [None, None, 7, None, None, 4],
    [None, None, 5, 2, 4, None]
]

print(dijkstra(grath, 0))