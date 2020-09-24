def sumRootToLeaf(self, root):
        partialSum = 0
        return findSumRootToLeaf(root, partialSum)

def findSumRootToLeaf(root, partialSum):
    if(root == None):
        return 0
    partialSum = partialSum * 2 + root.val
    if(root.left == None and root.right == None):
        return partialSum
    return findSumRootToLeaf(root.left, partialSum) + findSumRootToLeaf(root.right, partialSum)
