class Stack:
    def __init__(self):
        self.top = 0
        self.stack = []

    def push(self, val):
        self.stack.insert(self.top, val)
        self.top+=1
    
    def pop(self):
        self.stack.remove(self.stack[self.top-1])
        self.top-=1

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.stack)
stack1.pop()
print(stack1.stack)