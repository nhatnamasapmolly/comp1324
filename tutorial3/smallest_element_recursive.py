import bst

def smallest_element_recursive(bst):

    def find_smallest(node):
        if node.left is None:
            return node.key
        return find_smallest(node.left)
    
    if bst.root is None:
        return None
    
    return find_smallest(bst.root)


bst = bst.BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(10)
print("Smallest element in the BST:", smallest_element_recursive(bst))