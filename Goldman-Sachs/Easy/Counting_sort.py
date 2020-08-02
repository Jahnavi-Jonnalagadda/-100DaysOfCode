def countingSort(s,n):
    # code here
    arr_count = [0]*26
    
    arr_str = [0]*26
    
    for i in s:
        arr_str[ord(i)-ord("a")] = i
    
    for i in s:
        arr_count[ord(i)-ord("a")] += 1
    
    text = ""
    for i in range(len(arr_count)):
        if(arr_count[i]!=0):
            val = arr_str[i]*arr_count[i]
            text += val
    return text
