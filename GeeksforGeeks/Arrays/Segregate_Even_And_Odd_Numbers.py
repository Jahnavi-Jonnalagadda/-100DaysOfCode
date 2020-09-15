def segregateEvenOdd(arr):
    j = -1
    for i in range(len(arr)):
        if(arr[i] % 2 == 0):
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = list(map(int,input().split()))
print(segregateEvenOdd(arr))
