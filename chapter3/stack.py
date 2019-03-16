from .. chapter2 import Node as n

class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def peek(self):
        if self.isEmpty(): return None
        return self.head.value

    def push(self,value):
        node = n.Node(value,self.head)
        self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty(): return None

        val = self.head.value
        self.head = self.head.nextNode
        self.size -= 1
        return val

