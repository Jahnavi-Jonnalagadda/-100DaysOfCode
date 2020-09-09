def rotateString(A, B):
        if(len(A) != len(B)):
            return False
        A = A+A
        if(B in A):
            return True
        return False

s1 = input()
s2 = input()
print(rotateString(s1, s2))
