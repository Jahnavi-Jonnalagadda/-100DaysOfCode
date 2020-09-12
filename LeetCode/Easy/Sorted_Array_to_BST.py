def sortedArrayToBST(nums):
        return minimalTree(nums, 0, len(nums)-1)

def minimalTree(nums, low, high):
    if(low > high):
        return None
    mid = (low+high)//2
    root = TreeNode(nums[mid])
    root.left = minimalTree(nums, low, mid-1)
    root.right = minimalTree(nums, mid+1, high)
    return root
