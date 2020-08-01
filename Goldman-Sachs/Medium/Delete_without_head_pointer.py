'''
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you.
'''

def deleteNode(curr_node):
    #code here
    temp = curr_node.next
    curr_node.data = temp.data
    curr_node.next = temp.next
