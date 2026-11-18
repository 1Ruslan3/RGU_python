def numIslands(grid):
    if not grid:
        return 0
    
    count = 0

    def dfs(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
                         ]

print(numIslands(grid))
