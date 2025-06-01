class Node:
    """
    This will create a node with data provided
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly Linked List is a data structure where we only be able to move in one direction
    """

    def __init__(self):
        self.head = None 

    def traversal(self):
        if self.head == None:
            print("list is empty")
            return
        
        print("traversing")
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
    
    def insertAtTheBeginning(self, data):
        newNode = Node(data)        
        newNode.next = self.head
        self.head = newNode
        return self.head
    
    def insertBeforeTheNode(self,data,node):
        newNode = Node(data)
        if self.head == None:
            return "list is empty"
        elif self.head.data == node:
            newNode.next = self.head
            self.head = newNode
            return self.head
        else:
            prevNode = self.head
            while prevNode != None and prevNode.next != None:
                if prevNode.next.data == node:
                    newNode.next = prevNode.next
                    prevNode.next = newNode
                    return self.head
                else:
                    prevNode = prevNode.next
            else:
                return "cannot find the node"
            
    def insertAfterTheNode(self,node,data):
        newNode = Node(data)
        if self.head == None:
            return "list is Empty"
        elif self.head.data == node:
            newNode.next = self.head.next
            self.head.next = newNode
            return self.head
        else:
            currentNode = self.head
            while currentNode != None:
                if currentNode.data == node:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    return self.head
                else:
                    currentNode = currentNode.next
            else:
                return "cannot find the node"

    def insertAtTheEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            
            current_node.next = newNode
        return self.head
    
    def deleteTheFirstNode(self):
        if self.head == None:
            return "list is Empty"
        node = self.head
        self.head = self.head.next
        node.next = None
        del node

    def deleteTheLastNode(self):
        if self.head == None:
            return "list is Empty"
        elif self.head.next == None:
            node = self.head
            del node
            self.head = None
        else:
            prevNode = self.head
            while prevNode.next.next != None:
                prevNode = prevNode.next
            node = prevNode.next
            prevNode.next = None
            del node
        
    def deleteTheNode(self,deletingNode):
        if self.head == None:
            return "list is Empty"
        elif self.head.data == deletingNode:
            node = self.head
            self.head = self.head.next
            node.next = None
            del node
            return self.head
        else:
            prevNode = self.head
            while prevNode.next != None:
                if prevNode.next.data == deletingNode:
                    node = prevNode.next
                    prevNode.next = node.next
                    node.next = None
                    del node
                    return self.head
                else:
                    prevNode = prevNode.next
            else:
                print("cannot find the node")


# print(SinglyLinkedList().__doc__)

# Example 
           
"""
list1 = SinglyLinkedList()
list1.traversal()
list1.deleteTheFirstNode()
list1.traversal()
list1.insertAtTheBeginning(1)
list1.traversal()
list1.insertAtTheBeginning(2)
list1.traversal()
list1.insertAtTheEnd(3)
list1.insertAfterTheNode(1,4)
list1.traversal()
list1.deleteTheFirstNode()
list1.traversal()
list1.deleteTheLastNode()
list1.traversal()
list1.deleteTheNode(1)
list1.traversal()
list1.deleteTheNode(1)
"""