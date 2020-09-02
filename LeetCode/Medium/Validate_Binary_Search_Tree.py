def isValidBST(self, root):
        int_min = -4294967296
        int_max = 4294967296
        return BST(root, int_min, int_max)

def BST(root, minVal, maxVal):
    if(root == None):
        return True
    
    if(root.val > minVal and root.val < maxVal and BST(root.left, minVal, root.val) and BST(root.right, root.val, maxVal)):
        return True
    else:
        return False
