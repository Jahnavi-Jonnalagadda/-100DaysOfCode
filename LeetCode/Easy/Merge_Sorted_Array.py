def merge(A, B, m, n):
        p1 = m - 1
        p2 = n - 1
        f = m+n-1
        while(p1>=0 and p2>=0 and f>=0):
            if(A[p1] >= B[p2]):
                A[f] = A[p1]
                f -= 1
                p1 -= 1
            elif(A[p1] <= B[p2]):
                A[f] = B[p2]
                f -= 1
                p2 -= 1
        while(p2 >= 0):
            A[f] = B[p2]
            f -= 1
            p2 -= 1
        return A

A = list(map(int,input().split()))
B = list(map(int,input().split()))
m, n = map(int,input().split())
print(merge(A, B, m, n))
