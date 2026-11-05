class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def isEmpty (self):
        return self.top == -1

    def push (self, val):
        self.stack.append(val)
        self.top += 1

    def pop (self):
        if self.isEmpty():
            print("Stack Underload")
            return 

        self.top -= 1
        return self.stack.pop()

    def peek (self):
        if self.isEmpty():
            print("Stack is empty.")
            return

        return self.stack[self.top]

class MyQueue(object):
    def __init__(self):
        self.stack1 = Stack()  # front
        self.stack2 = Stack()  # back

    def push(self, x):
        self.stack2.push(x)
        
    def pop(self):
        if self.empty():
            print("Queue is empty")
            return

        if self.stack1.isEmpty():
            while not self.stack2.isEmpty():
                self.stack1.push(self.stack2.pop())

        return self.stack1.pop()

    def peek(self):
        if self.empty():
            print("Queue is empty")
            return 

        if self.stack1.isEmpty():
            while not self.stack2.isEmpty():
                self.stack1.push(self.stack2.pop())

        return self.stack1.peek()
        
    def empty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

