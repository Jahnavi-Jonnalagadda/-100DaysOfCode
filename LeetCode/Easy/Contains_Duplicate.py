# Approach 1: TC - O(NlogN) ; SC - O(1)
def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]):
                return True
        return False

# Approach 2: TC - O(N) ; SC - O(N)
def containsDuplicate(self, nums):
        dct = {}
        for i in range(len(nums)):
            if(nums[i] in dct):
                dct[nums[i]] += 1
            else:
                dct[nums[i]] = 1
        
        for item in dct:
            if(dct[item] > 1):
                return True
        return False
