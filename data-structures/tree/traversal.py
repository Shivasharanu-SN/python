class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def PreorderTraversal(self,node):

        if node == None:
            return
        
        print(node.data,end=' ')
        self.PreorderTraversal(node.left)
        self.PreorderTraversal(node.right)


    def InorderTraversal(self,node):

        if node == None:
            return
        
        self.InorderTraversal(node.left)
        print(node.data,end=' ')
        self.InorderTraversal(node.right)


    def PostorderTraversal(self,node):

        if node == None:
            return
        
        self.PostorderTraversal(node.left)
        self.PostorderTraversal(node.right)
        print(node.data,end=' ')

    def level_order_traversal_recursive(self,root):
        """BFS or Breadth First Search"""

        res = []
        self.level_order_traverse(root,0,res)
        return res

    def level_order_traverse(self,root,level,res):

        if root == None:
            return
        
        if len(res) <= level:
            res.append([])

        res[level].append(root.data)

        self.level_order_traverse(root.left, level+1, res)
        self.level_order_traverse(root.right, level+1, res)

    def level_order_traversal_iterative(self,root):

        if root == None:
            return []
        
        q = []
        res = []

        q.append(root)
        curr_level = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.pop(0)
                res[curr_level].append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            curr_level += 1

        return res
            

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    tree_obj = Tree()

    tree_obj.PreorderTraversal(root)
    print()
    tree_obj.InorderTraversal(root)
    print()
    tree_obj.PostorderTraversal(root)
    print()
    print(tree_obj.level_order_traversal_recursive(root))
    print(tree_obj.level_order_traversal_iterative(root))