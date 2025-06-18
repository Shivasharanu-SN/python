class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive Approach

# Function to find depth of a node
def find_depth(root, target, depth=0):
    if root is None:
        return -1
    if root.value == target:
        return depth
    left = find_depth(root.left, target, depth + 1)
    if left != -1:
        return left
    return find_depth(root.right, target, depth + 1)

# Function to find height of a node
def find_node(root, target):
    if root is None:
        return None
    if root.value == target:
        return root
    left = find_node(root.left, target)
    if left:
        return left
    return find_node(root.right, target)

def find_height(node):
    if node is None:
        return -1
    return 1 + max(find_height(node.left), find_height(node.right))




# Iterative Approach

from collections import deque

def find_depth_iterative(root, target_value):
    if not root:
        return -1
    queue = deque([(root, 0)])  # (node, depth)
    while queue:
        node, depth = queue.popleft()
        if node.value == target_value:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return -1  # not found

def find_node_iterative(root, target_value):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == target_value:
            return node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return None  # not found

from collections import deque

def find_height_iterative(node):
    if not node:
        return -1  # Convention: height of empty tree is -1

    queue = deque([node])
    height = -1

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        height += 1  # one level processed

    return height




# Example usage
if __name__ == "__main__":
    # Create tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    target_value = 10
    depth = find_depth(root, target_value)
    node = find_node(root, target_value)
    height = find_height(node)

    print(f"Depth of node {target_value} is {depth}")
    print(f"Height of node {target_value} is {height}")


