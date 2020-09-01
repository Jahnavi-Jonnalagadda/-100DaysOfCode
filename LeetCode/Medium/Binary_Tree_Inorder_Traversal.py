def inorderTraversal(root):
        if(root == None):
            return None
        st = []
        res = []
        curr = root
        
        while True:
            while(curr != None):
                st.append(curr)
                curr = curr.left
            if(len(st)>0):
                top = st.pop()
                res.append(top.val)
                curr = top.right
            else:
                break
        return res
