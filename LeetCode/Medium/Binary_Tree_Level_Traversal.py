def levelOrder(root):
        if(root == None):
            return None
        
        q = []
        res = []
        q.append(root)
        res.append([q[0].val])
        while(len(q)>0):
            p = len(q)
            s = []
            while(p>0):
                top = q.pop(0)
                if(top.left != None):
                    s.append(top.left.val)
                    q.append(top.left)
                if(top.right != None):
                    s.append(top.right.val)
                    q.append(top.right)
                p -= 1
            if(len(s)>0):
                res.append(s)
            else:
                break
        return res
