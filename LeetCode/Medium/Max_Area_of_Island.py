def maxAreaOfIsland(grid):
        if(len(grid) == 0):
            return 0
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    area = max(area, dfs(grid, rows, cols, i, j))
        return area

def dfs(grid, rows, cols, i, j):
    if(i<0 or j<0 or i>=rows or j>=cols or grid[i][j] == 0):
        return 0
    grid[i][j] = 0
    area = 1
    area += dfs(grid, rows, cols, i-1, j)
    area += dfs(grid, rows, cols, i+1, j)
    area += dfs(grid, rows, cols, i, j-1)
    area += dfs(grid, rows, cols, i, j+1)
    return area
