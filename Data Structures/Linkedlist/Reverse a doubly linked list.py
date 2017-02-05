def Reverse(head):
    temp=None
    curr=head
    while(curr is not None):
        temp=curr.prev
        curr.prev=curr.next
        curr.next=temp
        curr=curr.prev
    if temp is not None:
        head=temp.prev
    return head

  
  
