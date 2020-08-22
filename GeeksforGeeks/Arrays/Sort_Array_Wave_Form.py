def wave_array(arr):
    if(arr[0] < arr[1]):
        arr[0],arr[1] = arr[1],arr[0]
    i = 2
    while(i < len(arr)-1):
        if(arr[i] < arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
        if(arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        i += 2
    if(i == len(arr)-1):
        if(arr[i] < arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
    return arr

arr = [10, 5, 6, 3, 2, 20, 100, 80]
print(wave_array(arr))
