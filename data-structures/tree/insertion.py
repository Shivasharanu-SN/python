# Insertion in a binary tree (not necessarily a binary search tree) is 
# typically done using level-order traversal (BFS) to maintain balance — 
# i.e., insert in the first available spot from left to right.

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    new_node = Node(value)
    if not root:
        return new_node  # Tree was empty

    queue = deque([root])

    while queue:
        current = queue.popleft()

        if not current.left:
            current.left = new_node
            return root
        else:
            queue.append(current.left)

        if not current.right:
            current.right = new_node
            return root
        else:
            queue.append(current.right)

    return root  # shouldn't reach here normally
