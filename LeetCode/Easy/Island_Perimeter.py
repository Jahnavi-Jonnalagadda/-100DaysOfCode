def islandPerimeter(grid):
        if(len(grid) == 0):
            return 0
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    perimeter += 4
                    if(j-1 >= 0 and grid[i][j-1] == 1):
                        perimeter -= 2
                    if(i-1 >= 0 and grid[i-1][j] == 1):
                        perimeter -= 2
        return perimeter

grid = list(map(int,input().split()))
print(islandPerimeter(grid))
