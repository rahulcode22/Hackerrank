def MergeLists(headA, headB):
    if (headA is None and headB is None):
        return None
    if (headA is not None and headB is None):
        return headA
    if (headA is None and headB is not None):
        return headB
    if (headA.data <headB.data):
        headA.next=MergeLists(headA.next,headB)
    elif (headA.data >headB.data):
        temp=headB
        headB=headB.next
        temp.next=headA
        headA=temp
        headA.next=MergeLists(headA.next,headB)
    return headA
