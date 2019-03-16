from . import stack as s

class SetOfStacks(s.Stack):
    def __init__(self,tres):
        self.treshold = tres
        self.stacks = []
        self.stacks.append(s.Stack())

    def push(self,value):
        if self.stacks[-1].size() >= self.treshold: self.stacks.append(s.Stack())
        self.stacks[-1].push(value)

    def pop(self):
        self.stacks[-1].pop()
        if self.stacks[-1].isEmpty(): self.stacks.pop()
