def mergeSort(arr, low, high):
    if(low == high):
        return
    mid = (low+high)//2
    
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)    
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    p1 = low
    p2 = mid+1
    final_arr = [0]*(high-low+1)
    k = 0
    while(p1<=mid and p2<=high):
        if(arr[p1]<arr[p2]):
            final_arr[k] = arr[p1]
            p1 += 1
            k += 1
        else:
            final_arr[k] = arr[p2]
            p2 += 1
            k += 1
    while(p1<=mid):
        final_arr[k] = arr[p1]
        p1 += 1
        k += 1
    while(p2<=high):
        final_arr[k] = arr[p2]
        p2 += 1
        k += 1

    for i in range(low, high+1):
        arr[i] = final_arr[i-low]

arr = [10, 1, 2, 8, 5, 11, 3]
mergeSort(arr, 0, len(arr)-1)
print(arr)
            
