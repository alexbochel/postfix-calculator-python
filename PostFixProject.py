from __future__ import print_function

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
        self.stack.reverse()
        self.stack.remove(item) #Takes from beginning of the list not the end
        self.stack.reverse()
        self.index -= 1
        return item

class LogicalEval:

    def __init__(self, expression):
        self.stack = Stack()
        self.expression = expression

    def Not(self, expression):
        if (expression == '1'):
            return '0'
        else:
            return '1'

    def And(self, expression_one, expression_two):
        if (expression_two == expression_one):
            return '1'
        else:
            return '0'

    def Not_Equal(self, expression_one, expression_two):
        if (expression_one != expression_two):
            return '1'
        else:
            return '0'

    def Equal(self, expression_one, expression_two):
        if (expression_one == expression_two):
            return '1'
        else:
            return '0'

    def Or(self, expression_one, expression_two):
        if (expression_two == '1') or (expression_one == '1'):
            return '1'
        else:
            return '0'

    def Process_Expression(self):
        for character in self.expression:
            if (character == '1') or (character == '0'):
                self.stack.Push(character)
            elif (character == '='):
                new_value = self.Equal(self.stack.Pop(), self.stack.Pop())
                self.stack.Push(new_value)
            elif (character == '!'):
                new_value = self.Not(self.stack.Pop())
                self.stack.Push(new_value)
            elif (character == '&'):
                new_value = self.And(self.stack.Pop(), self.stack.Pop())
                self.stack.Push(new_value)
            elif (character == '|'):
                new_value = self.Or(self.stack.Pop(), self.stack.Pop())
                self.stack.Push(new_value)
            elif (character == '/'):
                new_value = self.Not_Equal(self.stack.Pop(), self.stack.Pop())
                self.stack.Push(new_value)

        return self.stack.Pop()

if __name__ == '__main__':
    log = open("output.txt", "w")

    logical_evaluator_trail_1 = LogicalEval(PF1)
    print(logical_evaluator_trail_1.Process_Expression(), file = log)

    logical_evaluator_trail_2 = LogicalEval(PF2)
    print(logical_evaluator_trail_2.Process_Expression(), file = log)

    logical_evaluator_trail_3 = LogicalEval('01=1/10|1/&')
    print(logical_evaluator_trail_3.Process_Expression(), file = log)

    logical_evaluator_trail_4 = LogicalEval('11=0/0!&1|')
    print(logical_evaluator_trail_4.Process_Expression(), file = log)

    logical_evaluator_trail_5 = LogicalEval('10&11!&|0/')
    print(logical_evaluator_trail_5.Process_Expression(), file = log)