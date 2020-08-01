<<<<<<< HEAD
def rotateArr(A,D,N):
    #Your code here
    D = D%N
    rev(A,0,D-1)
    rev(A,D,N-1)
    rev(A,0,N-1)
    return A

def rev(A, start, end):
    while(start<end):
        A[start],A[end] = A[end], A[start]
        start += 1
        end -= 1
||||||| 19dc72f
=======
def rotateArr(A,D,N):
    #Your code here
    D = D%N
    rev(A,0,D-1)
    rev(A,D,N-1)
    rev(A,0,N-1)
    return A

def rev(A, start, end):
    while(start<end):
        A[start],A[end] = A[end], A[start]
        start += 1
        end -= 1
>>>>>>> 66a4de8564a93a08701957d8f6260aca0920f9e0
