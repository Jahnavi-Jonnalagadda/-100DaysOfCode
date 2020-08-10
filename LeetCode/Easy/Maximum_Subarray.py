def maxSubArray(nums):
    curr_max = global_max = nums[0]
        
    for i in range(1, len(nums)):
        curr_max = max(nums[i], nums[i]+curr_max)
            
        if(curr_max > global_max):
            global_max = curr_max
                
    return global_max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
