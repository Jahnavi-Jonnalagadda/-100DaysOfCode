def preorderTraversal(root):
        if(root == None):
            return None
        
        st = []
        res = []
        st.append(root)
        while(len(st)>0):
            top = st.pop()
            res.append(top.val)
            if(top.right != None):
                st.append(top.right)
            if(top.left != None):
                st.append(top.left)
        return res
