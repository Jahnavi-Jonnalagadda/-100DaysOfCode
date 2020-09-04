def buildTree(self, inorder, postorder):
        if(len(inorder) == 0 or len(postorder) == 0):
            return None
        
        root = TreeNode(postorder[len(postorder)-1])
        idx = search(inorder, postorder[len(postorder)-1])
        
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:len(postorder)-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        
        return root

def search(arr, val):
    for i in range(len(arr)):
        if(arr[i] == val):
            return i
