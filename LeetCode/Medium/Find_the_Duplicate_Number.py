import sys
arr = [7,9,7,4,2,8,7,7,1,5]
arr.sort()
for i in range(len(arr)):
    if(arr[i] == arr[i+1]):
        print(arr[i])
        sys.exit()
