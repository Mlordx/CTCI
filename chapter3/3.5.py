from . import stack as s

class QueueByStacks(s.Stack):
    def __init__(self):
        self.s1 = s.Stack()
        self.s2 = s.Stack()

    def push(self,value):
        self.s1.push(value)
        
    def pop(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        self.s2.pop()
