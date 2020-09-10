def sparseSearch(arr, val):
    if(len(arr) == 0 or val == ""):
        return -1
    low = 0
    high = len(arr)-1
    while(low <= high):
        mid = (low+high)//2
        if(arr[mid] == val):
            return mid
        if(arr[mid] == ""):
            p = mid-1
            q = mid+1
            while True:
                if(p < low and q > high):
                    return -1
                if(p >= low and arr[p] != ""):
                    mid = p
                    break
                elif(q <= high and arr[q] != ""):
                    mid = q
                    break
                p += 1
                q -= 1
            if(arr[mid] == val):
                return mid
            elif(arr[mid] < val):
                low = mid+1
            else:
                high = mid-1
    return -1

arr = list(map(str, intput().split()))
val = input()
print(sparseSearch(arr, val))
