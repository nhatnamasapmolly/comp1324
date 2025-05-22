class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self):
        self.root = None

    def heapify(self, node):
        if node is None:
            return
    
        smallest = node
        if node.left and node.left.value < smallest.value:
            smallest = node.left
        if node.right and node.right.value < smallest.value:
            smallest = node.right
        
        if smallest != node:
            # Swap values and continue heapifying down
            node.value, smallest.value = smallest.value, node.value
            self.heapify(smallest)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    
    def _insert(self, current, value):
        print(current.value)
        if current is None:
            return Node(value)
        if value < current.value:
            current.value, value = value, current.value
            
        if current.left is None:
            current.left = Node(value)
        elif current.right is None:
            current.right = Node(value)
        else: 
            if self._height(current.left) <= self._height(current.right):
                current.left = self._insert(current.left, value)
            else:
                current.right = self._insert(current.right, value)
        self.heapify(current)
        return current
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
        
    def traverse(self):
        result = []
        self._traverse(self.root, result)
        return result
    def _traverse(self, node, result):
        if node:
            result.append(node.value)
            self._traverse(node.left, result)
            self._traverse(node.right, result)
        else:
            return None
        

# Example usage
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(15)
    print("Heap elements in level order:", heap.traverse())

# code heap again