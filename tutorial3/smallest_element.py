import bst

def find_smallest_element(bst):

    if bst.root is None:
        return None  

    current = bst.root
    while current.left is not None:
        current = current.left
    return current.key



bst = bst.BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
print("Smallest element in the BST:", find_smallest_element(bst))