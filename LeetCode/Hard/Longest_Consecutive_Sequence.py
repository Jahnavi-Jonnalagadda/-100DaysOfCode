# Approach 1: TC - O(NlogN) ; SC - O(1)
def longestConsecutive(arr):
    arr.sort()
    res = 0
    count = 0
    for i in range(1, len(arr)):
        if(arr[i]-arr[i-1] == 1):
            count += 1
        else:
            count = 1
        res = max(res, count)
    return res

# Approach 2: TC - O(N) ; SC - O(N)
def longestConsecutive(arr):
        values = list(set(arr))
        mx = 0
        for i in values:
            if(i - 1 in values):
                continue
            count = 1
            while(i+1 in values):
                count += 1
                i += 1
            mx = max(mx, count)
        return mx

arr = list(map(int,input().split()))
print(longestConsecutive(arr))
