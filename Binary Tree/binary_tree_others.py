#Height, Descendants, Ancestors, Leaves, Root, Parent, Children, Siblings
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def calculate_height(node):
    if node is None:
        return 0
    else:
        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)
        return max(left_height, right_height) + 1


def count_descendants(node):
    if node is None:
        return 0
    else:
        return count_descendants(node.left) + count_descendants(node.right) + 1


def count_ancestors(node):
    if node is None or (node.left is None and node.right is None):
        return 0
    else:
        return count_ancestors(node.left) + count_ancestors(node.right) + 1


def count_leaves(node):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return count_leaves(node.left) + count_leaves(node.right)


def find_root(node):
    if node is None:
        return None
    while node.left is not None or node.right is not None:
        if node.left is not None:
            node = node.left
        else:
            node = node.right
    return node


def find_parent(node, value):
    if node is None:
        return None
    if (node.left is not None and node.left.data == value) or (node.right is not None and node.right.data == value):
        return node
    parent = find_parent(node.left, value)
    if parent is not None:
        return parent
    else:
        return find_parent(node.right, value)


def find_children(node):
    children = []
    if node.left is not None:
        children.append(node.left.data)
    if node.right is not None:
        children.append(node.right.data)
    return children


def find_siblings(node, value):
    parent = find_parent(node, value)
    if parent is not None:
        if parent.left is not None and parent.left.data == value:
            if parent.right is not None:
                return [parent.right.data]
            else:
                return []
        elif parent.right is not None and parent.right.data == value:
            if parent.left is not None:
                return [parent.left.data]
            else:
                return []
    return []


# Membangun binary tree
root = Node(27)
root.left = Node(14)
root.right = Node(35)
root.left.left = Node(10)
root.left.right = Node(19)
root.right.left = Node(31)
root.right.right = Node(42)

# Contoh penggunaan
print("Height:", calculate_height(root))
print("Number of Descendants:", count_descendants(root))
print("Number of Ancestors:", count_ancestors(root))
print("Number of Leaves:", count_leaves(root))
print("Root:", find_root(root).data)
print("Parent of 10:", find_parent(root, 10).data)
print("Children of 27:", find_children(root))
print("Siblings of 19:", find_siblings(root, 19))
