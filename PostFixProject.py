
PF1 = "0!!!1/10&1!!&=1=0|"
PF2 = "10=!10/&11!0/=1|11!&|&0/"

class Stack:

    def __init__(self):
        self.stack = list()
        self.index = -1

    def Push(self, element):
        self.stack.append(element)
        self.index += 1

    def Pop(self):
        item = self.stack[self.index]
        self.index -= 1
        return item

class LogicalEval:

    def __init__(self, expression):
        self.stack = Stack()
        self.expression = expression







