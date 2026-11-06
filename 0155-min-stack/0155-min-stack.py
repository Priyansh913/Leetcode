class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.head = -1

    def isEmpty (self):
        return self.head == -1

    def push(self, value):
        self.stack.append(value)
        self.head += 1

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        self.stack.pop()
        self.min_stack.pop()

        self.head -= 1

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return
            
        return self.stack[self.head]

    def getMin(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        return self.min_stack[-1]
