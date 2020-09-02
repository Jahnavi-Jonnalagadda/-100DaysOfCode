def diameterOfBinaryTree(self, root):
        if(root == None):
            return 0
        left_hgt = height(root.left)
        right_hgt = height(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(left_hgt+right_hgt, max(left_diameter, right_diameter))

def height(root):
    if(root == None):
        return 0
    return 1+max(height(root.left), height(root.right))
