class Queue(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
queue = Queue()
queue.enqueue("red")
queue.enqueue("Purple")
queue.enqueue("Indigo")
queue.enqueue("Violet")
print(queue.size())
print(queue.dequeue())