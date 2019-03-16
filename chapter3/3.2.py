from . import stack as s

class StackWithMin(s.Stack):
    def __init__(self):
        super().__init__()
        self.minStack = s.Stack()

    def push(self, value):
        super().push(value)
        if self.minStack.isEmpty() or value < self.minStack.peek():
            self.minStack.push(value)

    def pop(self):
        if not super().isEmpty()
        value = super().pop()
        if value <= self.minStack.peek():
            self.minStack.pop()

    def seeMin(self):
        return self.minStack.peek()
