def SortedInsert(head, data):
    if (head is None):
        new_node=Node(data)
        return new_node
    if (head.data <=data):
        head.next=SortedInsert(head.next,data)
    elif (head.data>data):
        new_node=Node(data)
        new_node.next=head
        new_node.prev=head.prev
        head.prev=new_node
        head=new_node
    return head
    
