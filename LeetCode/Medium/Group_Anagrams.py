def groupAnagram(arr):
    dct = {}
    for i in range(len(arr)):
        p = arr[i]
        arr[i] = sortString(arr[i])
        if(arr[i] in dct):
            dct[arr[i]].append(p)
        else:
            dct[arr[i]] = [p]
    final_list = getAnagramList(dct)
    return final_list

def sortString(s):
    s = sorted(s)
    s = "".join(s)
    return s

def getAnagramList(dct):
    final_list = []
    for item in dct:
        final_list.append(dct[item])
    return final_list

arr = list(map(int,input().split()))
print(groupAnagram(arr))
            
        
