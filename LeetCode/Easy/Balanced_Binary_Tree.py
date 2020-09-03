def isBalanced(root):
        if(balancedHgt(root) == -1):
            return False
        return True

def balancedHgt(root):
    if(root == None):
        return 0
    lh = balancedHgt(root.left)
    rh = balancedHgt(root.right)
    
    if(lh == -1 or rh == -1 or abs(lh-rh)>1):
        return -1
    return 1 + max(lh, rh)
