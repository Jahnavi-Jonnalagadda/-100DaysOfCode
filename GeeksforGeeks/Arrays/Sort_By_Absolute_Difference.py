def sort_abs_diff(arr, x, result, abs_diff, dct):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        val = abs(x-arr[i])
        if val not in dct:
            dct[val] = [arr[i]]
        else:
            dct[val].append(arr[i])
        abs_diff.append(val)

    abs_diff.sort()
    for j in range(len(abs_diff)):
        if(len(dct[abs_diff[j]])>1):
            result.append(dct[abs_diff[j]][0])
            dct[abs_diff[j]].pop(0)
        else:
            result.append(*dct[abs_diff[j]])

    return result

t = int(input())
for p in range(t):
    n,x = map(int,input().split())
    arr = input().split()
    result = []
    abs_diff = []
    dct = {}
    print(*sort_abs_diff(arr, x, result, abs_diff, dct))
