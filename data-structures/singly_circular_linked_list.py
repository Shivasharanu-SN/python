class Node:
    """
    This will create a node with data provided
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    """
    Singly Circular Linked List is a data structure where we only be able to move in one direction but in a circular path
    """

    def __init__(self):
        self.head = None 

    def traversal(self):
        if self.head == None:
            print("list is empty")
            return
        
        print("traversing")
        current_node = self.head.next
        print(self.head.data)
        while current_node != self.head:
            print(current_node.data)
            current_node = current_node.next
    
    def insertAtTheBeginning(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
        else:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.next = self.head
            self.head = newNode
 
    def insertAtTheEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
        else:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.next = self.head
    
    def deleteTheFirstNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head == self.head.next:
            self.head = None
        else:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next
            node = self.head
            lastNode.next = node.next
            self.head = node.next
            node.next = None
            del node

    def deleteTheLastNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head.next == self.head:
            node = self.head
            del node
            self.head = None
        else:
            prevNode = self.head
            while prevNode.next.next != self.head:
                prevNode = prevNode.next
            node = prevNode.next
            prevNode.next = self.head
            node.next = None
            del node
        
    def deleteTheNode(self,deletingNode):
        if self.head == None:
            return "list is Empty"
        elif self.head.data == deletingNode:
            if self.head.next == self.head:
                node = self.head
                node.next = None
                self.head = None
            else:
                lastNode = self.head
                while lastNode.next != self.head:
                    lastNode = lastNode.next
                node = self.head
                self.head = self.head.next
                lastNode.next = self.head
                node.next = None
            del node
        else:
            prevNode = self.head
            while prevNode.next != self.head:
                if prevNode.next.data == deletingNode:
                    node = prevNode.next
                    prevNode.next = node.next
                    node.next = None
                    del node
                    break
                else:
                    prevNode = prevNode.next
            else:
                print("cannot find the node")


# print(SinglyCircularLinkedList().__doc__)

# Example 
           
"""
list1 = SinglyCircularLinkedList()
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