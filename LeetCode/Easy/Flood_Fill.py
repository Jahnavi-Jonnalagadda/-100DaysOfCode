def floodFill(image, sr, sc, newColor):
        if(newColor == image[sr][sc]):
            return image
        rows = len(image)
        cols = len(image[0])
        src = image[sr][sc]
        dfs(image, newColor, src, sr, sc, rows, cols)
        return image

def dfs(image, newColor, src, sr, sc, rows, cols):
    if(sr < 0 or sc >= cols or sr >= rows or sc < 0):
        return 
    elif(image[sr][sc] != src):
        return 
    image[sr][sc] = newColor
    dfs(image, newColor, src, sr-1, sc, rows, cols)
    dfs(image, newColor, src, sr+1, sc, rows, cols)
    dfs(image, newColor, src, sr, sc-1, rows, cols)
    dfs(image, newColor, src, sr, sc+1, rows, cols)
