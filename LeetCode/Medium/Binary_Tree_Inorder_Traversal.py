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
                curr = st.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                break
        return res
