def water_trap(A):
    n = len(A)
    if(n<3):
        return 0
    left_max = [0]*n
    right_max = [0]*n
	    
    left_max[0] = A[0]
    for i in range(1, len(A)):
        left_max[i] = max(left_max[i-1], A[i])
	    
    right_max[n-1] = A[n-1]
    for i in range(len(A)-2, -1, -1):
        right_max[i] = max(right_max[i+1], A[i])
	    
    water_amt = 0
    for i in range(n):
        water_amt = water_amt + min(left_max[i], right_max[i]) - A[i]
    return water_amt

arr = list(map(int,input().split()))
print(water_trap(arr))
