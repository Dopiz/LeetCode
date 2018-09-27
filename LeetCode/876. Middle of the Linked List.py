def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    count = 1
    top = head
    while head.next != None:
        count = count + 1
        head = head.next

    target = count // 2 + 1

    for i in range(target - 1):
        top = top.next
    
    return top