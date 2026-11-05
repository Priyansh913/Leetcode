class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def isEmpty (self):
        return self.top == -1

    def isFull (self):
        return self.top == self.size - 1

    def push (self, val):
        if self.isFull():
            print("Stack Overload")
            return 

        self.top += 1
        self.stack.append(val)

    def pop (self):
        if self.isEmpty():
            print("Stack Underload")
            return

        val = self.stack.pop()
        self.top -= 1
        return val

    def peek (self):
        if self.isEmpty():
            print("Stack Underload")
            return
        
        return self.stack[self.top]
        
class Solution(object):
    def isValid(self, s):
        stack = Stack(len(s))

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.push(ch)

            elif ch == ')':
                if stack.peek() == '(':
                    stack.pop()
                else:
                    return False

            elif ch == '}':
                if stack.peek() == '{':
                    stack.pop()
                else:
                    return False

            else:
                if stack.peek() == '[':
                    stack.pop()
                else:
                    return False

        return stack.isEmpty()

s = "()[]{}"
sol = Solution()

if sol.isValid(s):
    print("String is valid")

else:
    print("String is not valid")