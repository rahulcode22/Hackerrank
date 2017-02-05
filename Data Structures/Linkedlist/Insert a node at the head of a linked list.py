class Node(object):
 
   def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    return head

 

