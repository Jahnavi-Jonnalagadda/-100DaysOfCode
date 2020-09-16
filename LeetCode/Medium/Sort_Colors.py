# Approach 1:
def sortColors(nums):
        low = 0
        mid = 0
        high = len(nums)-1
        while(mid <= high):
            if(nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif(nums[mid] == 1):
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

# Approach 2:
def sortColors(arr):
        zero, one, two = 0, 0, 0
        for i in range(len(arr)):
            if(arr[i] == 0): zero+= 1
            if(arr[i] == 1): one += 1
            if(arr[i] == 2): two += 1

        i = 0
        while(zero > 0):
            arr[i] = 0
            zero -= 1
            i += 1
        while(one > 0):
            arr[i] = 1
            one -= 1
            i += 1
        while(two > 0):
            arr[i] = 2
            two -= 1
            i += 1
        return arr
