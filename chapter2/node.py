class Node:
    def __init__(self,value,n=None):
        self.value = value
        self.nextNode = n

    def length(node):
        l = 0
        while node is not None:
            l += 1
            node = node.nextNode
        return l

    def toString(node):
        string = ''
        while node.next is not None:
            string += str(node.value) + ", "
        string += str(node.value) + "."
        return string
