class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        
    def push(self, element):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(element)
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def top(self):
        if self.stack_1:
            return self.stack_1[-1]

    def pop(self):
        return self.stack_1.pop()

queue = MyQueue()
queue.push(1)
print(queue.pop())
queue.push(2)
queue.push(3)
print(queue.top())
print(queue.pop())
