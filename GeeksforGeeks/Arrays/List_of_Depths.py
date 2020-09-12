class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createLL(arr):
    root = LinkedList(arr[0])
    temp = root
    for i in range(1, len(arr)):
        node = LinkedList(arr[i])
        temp.next = node
        temp = temp.next
    printLL(root)

def printLL(root):
    temp = root
    while(temp != None):
        print(temp.val, end=" ")
        temp = temp.next
    print()
        
def listDeptBFS(root):
    if(root == None):
        return None
    curr = root
    q = []
    q.append(curr)
    preLevel = [curr.val]
    createLL(preLevel)
    nextLevel = []
    while(True):
        while(len(preLevel) > 0):
            preLevel.pop(0)
            u = q.pop(0)
            if(u.left != None):
                nextLevel.append(u.left.val)
                q.append(u.left)
            if(u.right != None):
                nextLevel.append(u.right.val)
                q.append(u.right)
        if(len(nextLevel) == 0):
            break
        else:
            createLL(nextLevel)
            preLevel = nextLevel
            nextLevel = []
'''
Sample Input:
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.left = TreeNode(60)
root.right.right =TreeNode(70)
listDeptBFS(root)
'''



        
        
