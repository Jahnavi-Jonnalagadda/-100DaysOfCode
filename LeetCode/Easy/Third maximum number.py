class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<3):
            return max(nums)
        
        int_min = -2147483648
        l1 = None
        l2 = None
        l3 = None

        for i in range(len(nums)):
            if(nums[i] == l1 or nums[i] == l2 or nums[i] == l3):
                continue
            else:
                if(nums[i] > l1):
                    l3 = l2
                    l2 = l1
                    l1 = nums[i]
                elif(nums[i]>l2):
                    l3 = l2
                    l2 = nums[i]
                elif(nums[i]>l3):
                    l3 = nums[i]
        if(l3 == None):
            return max(nums)
        else:
            return l3
