def twoSum(arr, k):
        for i in range(len(arr)):
                diff = k - arr[i]
                if(binary_search(arr, low, high, k) == True):
                        return True
                return False

'''def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i
        print(dct)
            
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                return [i, dct[diff]]'''

nums = [3,2,4]
target = 6
print(twoSum(nums,target))
