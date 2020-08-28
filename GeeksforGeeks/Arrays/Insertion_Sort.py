def insertion_sort(arr):
    for i in range(1, len(arr)):
        if(arr[i] < arr[i-1]):
            j = i
            while(arr[j] < arr[j-1] and j>0):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    return arr

arr = list(map(int,input().split()))
print(insertion_sort(arr))          
