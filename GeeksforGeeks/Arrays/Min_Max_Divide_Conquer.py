def min_max(arr, low, high):
    #INT_MIN and INT_MAX
    mx = 2147483648
    mn = -2147483648
    if(low == high):
        mx = arr[low]
        mn = arr[high]
        return (mx, mn)
    elif(low == high-1):
        if(arr[low]<arr[high]):
            mn = arr[low]
            mx = arr[high]
        else:
            mn = arr[high]
            mx = arr[low]
        return (mx, mn)
    else:
        mid = (low+high)//2
        mx1, mn1 = min_max(arr, low, mid)
        mx2, mn2 = min_max(arr, mid+1, high)
        mx = max(mx1, mx2)
        mn = min(mn1, mn2)
    return [mx, mn]

arr = list(map(int,input().split()))
MinMax = min_max(arr, 0, len(arr)-1)
print("Maximum Element: ", MinMax[0])
print("Minimum Element: ", MinMax[1])

