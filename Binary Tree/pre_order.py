class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


# Membangun binary tree
root = Node(27)
root.left = Node(14)
root.right = Node(35)
root.left.left = Node(10)
root.left.right = Node(19)
root.right.left = Node(31)
root.right.right = Node(42)

# Contoh penggunaan
print("Jalur pre-order:")
preorder_traversal(root)
