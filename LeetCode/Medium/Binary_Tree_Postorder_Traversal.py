def postorderTraversal(self, root):
        if(root == None):
            return None
        
        s1 = []
        s2 = []
        s1.append(root)
        while(len(s1)>0):
            top = s1.pop()
            s2.append(top.val)
            if(top.left != None):
                s1.append(top.left)
            if(top.right != None):
                s1.append(top.right)
        return s2[::-1]
