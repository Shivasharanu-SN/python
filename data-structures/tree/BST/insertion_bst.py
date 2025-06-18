class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst_recursive(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert_bst_recursive(root.left, value)
    else:
        root.right = insert_bst_recursive(root.right, value)

    return root

def insert_bst_iterative(root, value):
    new_node = Node(value)
    if root is None:
        return new_node

    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root
