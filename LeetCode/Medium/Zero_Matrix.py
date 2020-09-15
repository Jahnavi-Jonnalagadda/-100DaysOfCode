def setZeroes(arr):
        rows = len(arr)
        cols = len(arr[0])
        r, c = [], []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if(arr[i][j] == 0):
                    r.append(i)
                    c.append(j)

        for k in range(len(r)):
            for l in range(cols):
                arr[r[k]][l] = 0

        for b in range(rows):
            for a in range(len(c)):
                arr[b][c[a]] = 0
        return arr

arr = list(map(int,input().split()))
print(setZeroes(arr))
