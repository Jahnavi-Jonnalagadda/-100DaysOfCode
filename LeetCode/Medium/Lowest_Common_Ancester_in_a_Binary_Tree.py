def lowestCommonAncestor(root, p, q):
        if(root == None):
            return None
        if(root == p or root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if(left != None and right != None):
            return root
        return left if left != None else right
