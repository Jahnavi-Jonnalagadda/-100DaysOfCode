def buildTree(self, preorder, inorder):
        if(len(preorder)==0 or len(inorder)==0):
            return None
        root = TreeNode(preorder[0])
        idx = search(inorder, preorder[0])

        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])

        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root

def search(arr, value):
    for i in range(len(arr)):
        if(arr[i] == value):
            return i
