
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

    def Equal(self, expression_one, expression_two):
        if (expression_one == expression_two):
            return 1
        else:
            return 0

    def Process_Expression(self):
        for character in self.expression:
            if (character == '1') or (character == '0'):
                self.stack.push(character)
            elif (character == '='):
                new_value = self.Equal(self.stack.Pop(), self.stack.Pop())
                self.stack.Push(new_value)

def Main():
    logical_evaluator_trail_1 = LogicalEval(PF1)
    logical_evaluator_trail_1 = LogicalEval(PF2)
    logical_evaluator_trail_1 = LogicalEval('')
    logical_evaluator_trail_1 = LogicalEval('')
    logical_evaluator_trail_1 = LogicalEval('')











