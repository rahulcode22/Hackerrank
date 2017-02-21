def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)
