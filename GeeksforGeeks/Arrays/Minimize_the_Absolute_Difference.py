def abs_min(A, B, C):
    i = 0
    j = 0
    k = 0
    min_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
    
    while(i<len(A)-1 and j<len(B)-1 and k<len(C)-1):
        mn = min(A[i], B[j], C[k])
        if(mn == A[i]):
            i += 1
        elif(mn == B[j]):
            j += 1
        else:
            k += 1

        curr_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
        if(curr_diff < min_diff):
            min_diff = curr_diff

    return min_diff

A = [1, 4, 5, 8, 10]
B = [6, 9, 15]
C = [2, 3, 6, 6]
print(abs_min(A, B, C))
        

        
