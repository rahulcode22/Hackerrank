def Delete(head, position):
    if position == 0 :
        return head.next
    temp = head
    for _ in xrange(position):
        prevNode = temp
        temp=temp.next
    prevNode.next=temp.next
    return head
  
  
