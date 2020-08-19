def plus_one(arr):
    l = len(digits)
    for i in range(l-1,-1,-1):
        if(digits[i]<9):
            digits[i] += 1
            return digits
        digits[i] = 0
        
    final_array = [0]*(l+1)
    final_array[0] = 1
    return final_array

digits = list(map(int,input().split()))
print(plus_one(digits))
