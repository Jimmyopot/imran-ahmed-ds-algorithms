class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    # view last element
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push("Red")
stack.push("Blue")
stack.push("Green")
stack.push("Black")

print(stack.size())
print(stack.pop())
print(stack.isEmpty())

