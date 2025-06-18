class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def delete_bst_node(root, key):
    if root is None:
        return None

    if key < root.value:
        root.left = delete_bst_node(root.left, key)
    elif key > root.value:
        root.right = delete_bst_node(root.right, key)
    else:
        # Node found
        # Case 1: No child
        if root.left is None and root.right is None:
            return None
        # Case 2: One child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Case 3: Two children
        else:
            # Find in-order successor (min in right subtree)
            successor = get_min_node(root.right)
            root.value = successor.value
            root.right = delete_bst_node(root.right, successor.value)

    return root

def get_min_node(node):
    current = node
    while current.left:
        current = current.left
    return current
