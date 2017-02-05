def ReversePrint(head):
    prev=None
    current=head
    while(current is not None):
        next=current.next
        current.next=prev
        prev=current
        current=next
    head=prev
    temp=head
    while(temp):
        print temp.data
        temp=temp.next
