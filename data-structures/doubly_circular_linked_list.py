class Node:
    """
    This will create a node with data provided
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    """
    Doubly Circular Linked List is a data structure where we will be able to move in both direction and in a circular path
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def traversal(self):
        if self.head == None:
            print("list is empty")
            return
        
        print("Forward Traversing")
        currentNode = self.head.next
        print(self.head.data)
        while currentNode != self.head:
            print(currentNode.data)
            currentNode = currentNode.next

        print('Backward Traversing')
        currentNode = self.tail.prev
        print(self.tail.data)
        while currentNode != self.tail:
            print(currentNode.data)
            currentNode = currentNode.prev
        
    
    def insertAtTheBeginning(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
            newNode.prev = newNode.next = self.head
        else:
            newNode.next = self.head
            newNode.prev = self.head.prev
            newNode.prev.next = newNode
            self.head.prev = newNode
            self.head = newNode
    
    def insertAtTheEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
            newNode.prev = newNode.next = self.head
        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
    
    def deleteTheFirstNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head == self.tail:
            node = self.head
            node.prev = node.next = None
            self.head = self.tail = None
        else:
            node = self.head
            self.head = node.next
            self.head.prev = self.tail
            self.tail.next = self.head
            node.prev = node.next = None
        del node

    def deleteTheLastNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head == self.tail:
            node = self.head
            node.prev = node.next = None
            self.head = self.tail = None
        else:
            node = self.tail
            self.tail = node.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            node.prev = node.next = None
        del node
        
    def deleteTheNode(self,deletingNode):
        if self.head == None:
            return "list is Empty"
        else:
            currentNode = self.head
            if currentNode.data == deletingNode:
                if currentNode == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = currentNode.next
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                currentNode.prev = currentNode.next = None
                del currentNode
                return
            currentNode = currentNode.next
            while currentNode != self.head:
                if currentNode.data == deletingNode:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                    currentNode.prev = currentNode.next = None
                    del currentNode
                    break
                currentNode = currentNode.next
            else:
                print("cannot find the node")


# print(DoublyCircularLinkedList().__doc__)

# Example 
           
"""
list1 = DoublyCircularLinkedList()
list1.traversal()
list1.deleteTheFirstNode()
list1.traversal()
list1.insertAtTheBeginning(1)
list1.traversal()
list1.insertAtTheBeginning(2)
list1.traversal()
list1.insertAtTheEnd(3)
list1.traversal()
list1.deleteTheFirstNode()
list1.traversal()
list1.deleteTheLastNode()
list1.traversal()
list1.deleteTheNode(1)
list1.traversal()
list1.deleteTheNode(1)
"""