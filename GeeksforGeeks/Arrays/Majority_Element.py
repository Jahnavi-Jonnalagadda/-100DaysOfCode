def majority_elem(arr):
    dct = {}
    for i in range(len(arr)):
        if arr[i] not in dct:
            dct[arr[i]] = 1
        else:
            dct[arr[i]] += 1

    mx = 0
    for item in dct:
        if(dct[item]>mx):
            mx = item
    return mx

arr = [3,3,4,2,4,4,2,4,4]
print(majority_elem(arr))
