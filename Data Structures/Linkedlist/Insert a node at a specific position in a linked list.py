class Node(object):
 
   def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
def InsertNth(head, data, position):
    if position == 0 :
        return Node(data,head)
    temp = head
    for _ in xrange(position):
        prevNode = temp
        temp=temp.next
    prevNode.next = Node(data,temp)
    return head
  
