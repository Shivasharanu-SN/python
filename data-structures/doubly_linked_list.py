class Node:
    """
    This will create a node with data provided
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Doubly Linked List is a data structure where we will be able to move in both direction
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def traversal(self):
        if self.head == None:
            print("list is empty")
            return
        
        print("Forward Traversing")
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

        print('Backward Traversing')
        current_node = self.tail
        while current_node != None:
            print(current_node.data)
            current_node = current_node.prev
        
    
    def insertAtTheBeginning(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def insertAtTheEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            currentNode = self.tail        
            currentNode.next = newNode
            newNode.prev = currentNode
            self.tail = newNode
    
    def deleteTheFirstNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head == self.tail:
            node = self.head
            del node
            self.head = self.tail = None
        else:
            node = self.head
            self.head = node.next
            self.head.prev = None
            node.next = None
            del node

    def deleteTheLastNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head == self.tail:
            node = self.head
            del node
            self.head = self.tail = None
        else:
            node = self.tail
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            del node
        
    def deleteTheNode(self,deletingNode):
        if self.head == None:
            return "list is Empty"
        else:
            currentNode = self.head
            while currentNode != None:
                if currentNode.data == deletingNode:
                    if currentNode.prev == None and currentNode.next == None:
                        self.head = self.tail = None
                    elif currentNode.prev == None:
                        self.head = currentNode.next
                        currentNode.next = None
                    elif currentNode.next == None:
                        self.tail = currentNode.prev
                        currentNode.prev = None
                    else:
                        currentNode.prev.next = currentNode.next
                        currentNode.next.prev = currentNode.prev
                        currentNode.next = currentNode.prev = None
                    del currentNode
                    break
                currentNode = currentNode.next
            else:
                print("cannot find the node")


# print(DoublyLinkedList().__doc__)

# Example 
           
"""
list1 = DoublyLinkedList()
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