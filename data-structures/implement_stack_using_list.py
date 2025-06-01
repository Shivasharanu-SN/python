
class Stack:
    """
    Stack is a data structure which follows Last-In-First-Out (LIFO)
    Stack Operations :
    1. push
    2. pop
    3. peek
    """
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True 
        return False 

    def push(self, item):
        self.stack.append(item)
        return f"{item} is pushed into stack"

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return f"popped item is {self.stack.pop()}"

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return f"last item in the stack is {self.stack[-1]}"


# print(Stack().__doc__)

# Example
"""
stack1 = Stack()

print(stack1.push(1))
print(stack1.push(2))
print(stack1.push(3))
print(stack1.push(4))
print(stack1.push(5))
print(stack1.peek())
print(stack1.pop())
print(stack1.peek())
print(stack1.isEmpty())
"""