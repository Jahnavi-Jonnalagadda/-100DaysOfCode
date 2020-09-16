# Approach-1
def plus_one(arr):
    n = len(arr)
    arr[n-1] += 1
    carry = arr[n-1]//10
    arr[n-1] = arr[n-1]%10

    for i in range(n-2, -1, -1):
        if(carry == 1):
            arr[i] += 1
            carry = arr[i]//10
            arr[i] = arr[i]%10

    if(carry == 1):
        arr.insert(0, 1)
    return arr

# Approach-2
def plus_one(arr):
    if(arr == [9]):
        return [1, 0]
    n = len(arr)
    c = 0
    val = arr[n-1] + 1
    if(val > 9):
        arr[n-1] = 0
        c = 1
    else:
        arr[n-1] = val
    for i in range(len(arr)-2, -1, -1):
        if(arr[i] + c > 9 and i!=0):
            arr[i] = 0
            c = 1
        elif(arr[i] + c > 9 and i ==0):
            arr[i] = arr[i]+c
        else:
            arr[i] = arr[i]+c
            c = 0
    if(arr[0] > 9):
        return resize(arr)
    return arr

def resize(arr):
    arr.insert(0, 1)
    arr[1] = 0
    return arr

arr = list(map(int,input().split()))
print(plus_one(arr))
