def threeSum(nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if(i== 0 or nums[i] != nums[i-1]):
                start = i+1
                end = len(nums)-1

                while(start < end):

                    curr = nums[i]+nums[start]+nums[end]
                    if(curr == 0):
                        res.append([nums[i], nums[start], nums[end]])

                        while(start < end and nums[start] == nums[start+1]):
                            start += 1

                        while(start < end and nums[end] == nums[end-1]):
                            end -= 1

                        start += 1
                        end -= 1

                    elif(curr < 0):
                        start += 1

                    else:
                        end -= 1
        return res
