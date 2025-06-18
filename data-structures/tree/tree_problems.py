# printing all leaf nodes from left to right recursive and iterative approach

def print_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.value, end=" ")
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

def print_leaf_nodes_iterative(root):
    if not root:
        return
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            result.append(node.value)
        # Push right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    for val in result:
        print(val, end=" ")


# find parent of the node recursive and iterative approach

def find_parent_recursive(root, target, parent=None):
    if root is None:
        return None
    if root.value == target:
        return parent
    left = find_parent_recursive(root.left, target, root)
    if left:
        return left
    return find_parent_recursive(root.right, target, root)


from collections import deque

def find_parent_iterative(root, target):
    if not root or root.value == target:
        return None  # root has no parent

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            if node.left.value == target:
                return node
            queue.append(node.left)
        if node.right:
            if node.right.value == target:
                return node
            queue.append(node.right)
    return None  # not found



