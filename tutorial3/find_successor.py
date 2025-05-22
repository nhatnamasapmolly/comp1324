import bst

def find_successor(bst, key):
    # Helper function to find the node with the given key
    def find_node(node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return find_node(node.left, key)
        return find_node(node.right, key)

    # Helper function to find the minimum value in a subtree
    def find_min(node):
        while node.left is not None:
            node = node.left
        return node

    # Find the target node
    target_node = find_node(bst.root, key)
    if target_node is None:
        return None  # Key not found in the BST

    # Case 1: Node has a right subtree
    if target_node.right is not None:
        return find_min(target_node.right).key

    # Case 2: Node does not have a right subtree
    successor = None
    current = bst.root
    while current is not None:
        if target_node.key < current.key:
            successor = current
            current = current.left
        elif target_node.key > current.key:
            current = current.right
        else:
            break

    return successor.key if successor else None



# Example usage
if __name__ == "__main__":
    bst = bst.BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    key = 50
    successor = find_successor(bst, key)
    print(bst.inorder_traversal())
    if successor:
        print(f"The successor of {key} is {successor}.")
    else:
        print(f"There is no successor for {key}.")