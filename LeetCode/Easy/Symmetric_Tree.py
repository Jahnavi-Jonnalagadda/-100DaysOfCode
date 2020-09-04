# Iterative version
def isSymmetric(self, root):
        if(root == None):
            return True
        q = []
        res = []
        q.append(root)
        while(len(q)>0):
            p = len(q)
            s = []
            while(p > 0):
                top = q.pop(0)
                if(top != None):
                    s.append(top.val)
                    q.append(top.left)
                    q.append(top.right)
                else:
                    s.append("None")
                p -= 1
            if(s != s[::-1]):
                return False
        return True

# Recursive version
def isSymmetric(root):
        if(root == None):
            return True
        return check_symmetry(root.left, root.right)
        
def check_symmetry(leftNode, rightNode):
    if(leftNode == None or rightNode == None):
        return leftNode == rightNode
    
    if(leftNode.val != rightNode.val):
        return False
    return check_symmetry(leftNode.left, rightNode.right) and check_symmetry(leftNode.right, rightNode.left)
