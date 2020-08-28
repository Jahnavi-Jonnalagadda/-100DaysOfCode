def numIslands(grid):
        if(len(grid) == 0):
            return 0
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1"):
                    count += 1
                    dfs(grid, rows, cols, i, j)
        return count

def dfs(grid, rows, cols, i, j):
    if(i<0 or j<0 or i>rows-1 or j>cols-1 or grid[i][j] != "1"):
        return
    
    grid[i][j] = "2"
    
    dfs(grid, rows, cols, i, j+1)
    dfs(grid, rows, cols, i+1, j)
    dfs(grid, rows, cols, i, j-1)
    dfs(grid, rows, cols, i-1, j)
