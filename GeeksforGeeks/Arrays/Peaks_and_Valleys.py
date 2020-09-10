# Approach - 1: TC - O(NlogN) ; SC - O(1)
def peak_valley(arr):
    arr.sort()
    for i in range(1, len(arr), 2):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

# Approach - 2: TC - O(N) ; SC: O(1)
def peak_valley(arr):
    mx_idx = 0
    for i in range(1, len(arr)-1, 2):
        mx = max(arr[i], arr[i-1], arr[i+1])
        if(mx == arr[i]):
            continue
        elif(mx == arr[i-1]):
            mx_idx = i-1
        else:
            mx_idx = i+1
        arr[mx_idx], arr[i] = arr[i], arr[mx_idx]
    return arr

arr = list(map(int,input().split()))
print(peak_valley(arr))
