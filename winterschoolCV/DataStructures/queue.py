class Queue:
    def __init__(self):
        self.tail = 0
        self.queue = []

    def push(self, val):
        self.queue.insert(self.tail, val)
        self.tail+=1
    
    def remove(self):
        self.queue.remove(self.queue[0])
        self.tail-=1

queue1 = Queue()
queue1.push(1)
queue1.push(2)
queue1.push(3)
print(queue1.queue)
queue1.remove()
print(queue1.queue)