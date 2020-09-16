def canJump(nums):
        validIndex = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if(i+nums[i] >= validIndex):
                validIndex = i
        return validIndex == 0

nums = list(map(int,input().split()))
print(canJump(nums))
