
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

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = Stack()

        for current_idx in range(len(temperatures)):
            while not stack.isEmpty() and temperatures[current_idx] > temperatures[stack.peek()]:
                popped_idx = stack.pop()
                waiting = current_idx - popped_idx    
                answer[popped_idx] = waiting
            
            stack.push(current_idx)

        return answer
 
temperatures = [73,74,75,71,69,72,76,73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))