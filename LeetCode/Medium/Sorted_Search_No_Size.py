def search(arr, val):
    idx = 1
    while(arr[idx] != -1 and arr[idx] < val):
        idx *= 1
    return binarySearch(arr, val, idx//2, idx)

def binarySearch(arr, val, low, high):
    while(low <= high):
        mid = (low + mid)//2
        if(arr[mid] == val):
            return mid
        elif(arr[mid] < val):
            low = mid+1
        elif(arr[mid] > val or arr[mid] != -1):
            high = mid-1
    return -1
