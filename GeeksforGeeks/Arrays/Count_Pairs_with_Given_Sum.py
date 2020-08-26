def count_pairs(arr, k):
    start = 0
    end = len(arr)-1
    count = 0
    while(start < end):
        if(arr[start] + arr[end] > k):
            end -= 1
        elif(arr[start] + arr[end] < k):
            start += 1
        else:
            if(arr[start] != arr[end]):
                i = start
                while(start < end and arr[start] == arr[start+1]):
                    start += 1
                c1 = start-i+1
                j = end
                while(start < end and arr[end] == arr[end-1]):
                    end -= 1
                c2 = end-j+1
                count = count + (c1*c2)
                start += 1
                end -= 1
            else:
                val = (end-start+1)*(end-start)//2
                count = count + val
    return count

arr = list(map(int, input().split()))
k = 5
print(count_pairs(arr, k))
            
