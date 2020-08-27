def findPeakElement(nums):
        n = len(nums)
        return peak_element(nums, 0, n-1)

def peak_element(nums, start, end):
    mid = (start + end)//2
    if((mid == 0 or nums[mid]>=nums[mid-1]) and (mid == end or nums[mid]>=nums[mid+1])):
        return mid
    elif(mid<end and nums[mid]<nums[mid+1]):
        return peak_element(nums, mid+1, end)
    else:
        return peak_element(nums, start, mid-1)

    # The elif and else statements in the function above and comments below, both
    # wull work
    '''elif(mid > 0 and nums[mid] < nums[mid-1]):
        return peak_element(nums, start, mid-1)
    else:
        return peak_element(nums, mid+1, end)'''

anums = list(map(int,input().split()))

