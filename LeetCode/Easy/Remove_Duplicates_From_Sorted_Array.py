nums = [0,0,1,1,1,2,2,3,3,4]

start = 0
for i in range(1,len(nums)):
    if(nums[start]!=nums[i]):
        start += 1
        nums[start] = nums[i]
print(start+1)
