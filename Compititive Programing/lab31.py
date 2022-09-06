# Make BST from unsorted array


from typing import List


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
 
def insert(root, value):
    if root is None:
        return BST(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=' ')
    inorder(root.right)
    
def number_of_leafs(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return number_of_leafs(root.left) + number_of_leafs(root.right)

def number_of_levels(root):
    if root is None:
        return 0
    return 1 + max(number_of_levels(root.left), number_of_levels(root.right))
    
arr = [5,6,2,9,133,24,3524,133,53,10,33]
head = BST(arr[0])
for i in arr[1:]:
    insert(head, i)
inorder(head)
print(f"\nnumber of leaf nodes : {number_of_leafs(head)}")
print(f"number of levels : {number_of_levels(head)}")
    

    
    
    
    
        
    