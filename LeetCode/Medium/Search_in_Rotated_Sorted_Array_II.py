def searchRotatedArray(arr, target):
        low = 0
        high = len(arr) - 1
        while(low <= high):
            mid = (low+high)//2
            if(arr[mid] == target):
                return True
            if(arr[low] == arr[mid] == arr[high]):
                low += 1
                high -= 1
            elif(arr[low] <= arr[mid]):
                if(target >= arr[low] and target < arr[mid]):
                    high = mid-1
                else:
                    low = mid+1
            elif(arr[high] >= arr[mid]):
                if(target > arr[mid] and target <= arr[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return False

arr = list(map(int,input().split()))
target = int(input())
print(searchRotatedArray(arr, target))
