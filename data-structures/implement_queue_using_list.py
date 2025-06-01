class Queue:
    """
    Queue is a data structure which follows First-In-First-Out (FIFO)
    Queue Operations:
    1. enqueue (add item to queue)
    2. dequeue (remove item from queue)
    3. peek (check first item)
    """

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def enqueue(self, item):
        self.queue.append(item)
        return f"{item} is added to the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty so nothing can be removed"
        return f"{self.queue.pop(0)} is removed from the queue"
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return f"{self.queue[0]} is the first item now in the queue"


# print(Queue().__doc__)

#Example
"""
queue1 = Queue()
print(queue1.enqueue(1))
print(queue1.enqueue(2))
print(queue1.peek())
print(queue1.dequeue())
print(queue1.dequeue())
print(queue1.dequeue())
print(queue1.peek())
"""