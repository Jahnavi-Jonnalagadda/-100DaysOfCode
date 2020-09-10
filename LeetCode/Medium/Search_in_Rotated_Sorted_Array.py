def searchRotatedArray(arr, target):
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (low+high)//2
            if(nums[mid] == target):
                return mid
            if(nums[low] == nums[mid] == nums[high]):
                low += 1
                high -= 1
            elif(nums[low] <= nums[mid]):
                if(target >= nums[low] and target < nums[mid]):
                    high = mid-1
                else:
                    low = mid+1
            elif(nums[high] >= nums[mid]):
                if(target > nums[mid] and target <= nums[high]):
                    low = mid+1
                else:
                    high = mid-1
        return -1

arr = list(map(int,input().split()))
target = int(input())
print(searchRotatedArray(arr, target))
