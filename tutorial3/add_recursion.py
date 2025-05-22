import bst as bst
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def add_recusive(bst, value):
    if bst.root is None:
        bst.root = Node(value)
    else:
        _add_recursive(bst.root, value)
def _add_recursive(current, value):
    print(current.key)
    if value < current.key:
        if current.left is None:
            current.left = Node(value)  
        else:
            _add_recursive(current.left, value)
    
    elif value > current.key:
        if current.right is None:
            current.right = Node(value) 
        else:
            _add_recursive(current.right, value)

    else:
        return None
    


tree = bst.BinarySearchTree()
add_recusive(tree, 50)
add_recusive(tree, 30)
add_recusive(tree, 70)
add_recusive(tree, 20)


print(tree.inorder_traversal())