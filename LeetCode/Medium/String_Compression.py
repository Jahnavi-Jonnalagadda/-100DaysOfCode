def compress(arr):
        count = 1
        final_arr = []
        for i in range(len(arr)-1):
            if(arr[i] != arr[i+1]):
                final_arr.append(arr[i])
                final_arr.append(count)
                count = 1
            else:
                count += 1
        final_arr.append(arr[i])
        final_arr.append(count)
        l = len(final_arr)
        return l

arr = list(map(str, input().split()))
print(compress(arr))
