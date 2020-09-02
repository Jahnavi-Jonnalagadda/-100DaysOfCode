def invertTree(root):
    if(root == None):
        return None
        
    temp = root.left
    root.left = root.right
    root.right = temp
        
    invertTree(root.left)
    invertTree(root.right)
    return root
