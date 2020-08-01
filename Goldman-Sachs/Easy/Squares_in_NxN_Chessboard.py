def cntSquares(n):
    return (n*(n+1)*(2*n+1))//6

t = int(input())
for i in range(t):
    N = int(input())
    print(cntSquares(N))
