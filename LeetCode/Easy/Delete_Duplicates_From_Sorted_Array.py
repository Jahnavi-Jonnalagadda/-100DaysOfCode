def removeDup(arr):
    i, j = 1, 0
    while(i <len(arr)):
        if(arr[i] != arr[j]):
            j += 1
            arr[j] = arr[i]
        i += 1
    return j+1

arr = list(map(int,input().split()))
print(removeDup(arr))
            
