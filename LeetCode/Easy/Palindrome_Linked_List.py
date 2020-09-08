# Approach 1: TC - O(N) ; SC - O(N)
def palindrome(head):
    if(head == None):
        return True
    temp = head
    arr = []
    while(temp != None):
        arr.append(temp.val)
        temp = temp.next
    return checkPalindrome(arr)

def checkPalindrome(arr):
    p = 0
    q = len(arr)-1
    while(p <= q):
        if(arr[p] != arr[q]):
            return False
        p += 1
        q -= 1
    return True

# Approach 2: TC -O(N) ; SC - O(1)
def checkPalindrome(head):
    if(head == None):
            return True
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        fast = head
        slow = reverseList(slow)
        return compareLists(fast, slow)

def compareLists(temp, temp1):
    temp1 = reverseList(temp1)
    while(temp != None and temp1 != None):
        if(temp.val != temp1.val):
            return False
        temp = temp.next
        temp1 = temp1.next
    return True

def reverseList(temp1):
    t = temp1
    ptemp = None
    curr = t
    while(t != None):
        t = t.next
        curr.next = ptemp
        ptemp = curr
        curr = t
    return ptemp
        
