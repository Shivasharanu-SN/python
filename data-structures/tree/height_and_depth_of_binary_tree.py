class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
