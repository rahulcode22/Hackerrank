class Node(object):
 
   def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
def Insert(head, data):
    new_node=Node(data)
    if head is None:
        head=new_node
        return head
    last=head
    while(last.next):
        last=last.next
    last.next=new_node
    return  head
    
