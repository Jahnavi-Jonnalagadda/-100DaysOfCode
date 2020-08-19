def quick_sort(arr, low, high):
    if(low>=high):
        return
    part_idx = partition(arr, low, high)
    quick_sort(arr, low, part_idx)
    quick_sort(arr, part_idx+1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        while(arr[i]<pivot):
            i += 1
        while(arr[j]>pivot):
            j -= 1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[low],arr[j] = arr[j],arr[low]
    return j

arr = list(map(int,input().split()))
n = len(arr)-1
quick_sort(arr, 0, n)
print(arr)
