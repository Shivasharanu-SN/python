from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 1–4 in one function
def delete_node_bt(root, key):
    if not root:
        return None
    if root.left is None and root.right is None:
        return None if root.value == key else root

    key_node = None
    queue = deque([root])
    last_node = None
    parent_of_last = None

    while queue:
        last_node = queue.popleft()

        if last_node.value == key:
            key_node = last_node

        if last_node.left:
            parent_of_last = last_node
            queue.append(last_node.left)
        if last_node.right:
            parent_of_last = last_node
            queue.append(last_node.right)

    if key_node:
        key_node.value = last_node.value  # Step 3
        # Step 4: Delete deepest node
        if parent_of_last.right == last_node:
            parent_of_last.right = None
        elif parent_of_last.left == last_node:
            parent_of_last.left = None

    return root
