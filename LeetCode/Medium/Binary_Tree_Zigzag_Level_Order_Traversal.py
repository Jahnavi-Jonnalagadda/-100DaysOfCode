def zigzagLevelOrder(root):
        if(root == None):
            return None
        curr = root
        res = []
        q = []
        q.append(root)
        level = 0
        while(len(q)>0):
            p = len(q)
            s = []
            while(p>0):
                top = q.pop(0)
                s.append(top.val)
                if(top.left != None):
                    q.append(top.left)
                if(top.right != None):
                    q.append(top.right)
                p -= 1
            if(level%2 != 0):
                res.append(s[::-1])
            else:
                res.append(s)
            level += 1
        return res
