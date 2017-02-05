def RemoveDuplicates(head):
    if (head is None):
        return None
    nextitem=head.next
    while(nextitem is not None and head.data == nextitem.data):
        nextitem=nextitem.next
    head.next = RemoveDuplicates(nextitem)
    return head
    
