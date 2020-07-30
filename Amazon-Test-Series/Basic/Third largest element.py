if(len(arr)<3):
        return -1
        
    int_min = -2147483648
    l1 = int_min
    l2 = int_min
    l3 = int_min

    for i in range(len(arr)):
        if(arr[i] > l1):
            l3 = l2
            l2 = l1
            l1 = arr[i]
        elif(arr[i]>l2):
            l3 = l2
            l2 = arr[i]
        elif(arr[i]>l3):
            l3 = arr[i]
    return l3
