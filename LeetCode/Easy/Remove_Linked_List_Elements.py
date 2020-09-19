def removeElements(head, val):
        while(head != None and head.val == val):
            head = head.next
        temp = head
        while(temp != None and temp.next != None):
            if(temp.next.val == val):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
