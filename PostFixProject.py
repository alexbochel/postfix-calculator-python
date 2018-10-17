from __future__ import print_function

PF1 = "0!!!1/10&1!!&=1=0|"
PF2 = "10=!10/&11!0/=1|11!&|&0/"
TOS = 0


class LogicalEval:
    def __init__(self, expression):
        self.stack = [0] * 30
        self.expression = expression
        self.counter = 0

    def Push(self, element):
        self.stack[self.counter] = element
        self.counter += 1

    def Pop(self):
        self.counter -= 1
        item = self.stack[self.counter]
        return item

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
                self.Push(character)
            elif (character == '='):
                new_value = self.Equal(self.Pop(), self.Pop())
                self.Push(new_value)
            elif (character == '!'):
                new_value = self.Not(self.Pop())
                self.Push(new_value)
            elif (character == '&'):
                new_value = self.And(self.Pop(), self.Pop())
                self.Push(new_value)
            elif (character == '|'):
                new_value = self.Or(self.Pop(), self.Pop())
                self.Push(new_value)
            elif (character == '/'):
                new_value = self.Not_Equal(self.Pop(), self.Pop())
                self.Push(new_value)

        return self.stack[TOS]

if __name__ == '__main__':
    log = open("output.txt", "w")

    logical_evaluator_trail_1 = LogicalEval(PF1)
    print(PF1 + ": " + logical_evaluator_trail_1.Process_Expression(), file = log)

    logical_evaluator_trail_2 = LogicalEval(PF2)
    print(PF2 + ": " + logical_evaluator_trail_2.Process_Expression(), file = log)

    logical_evaluator_trail_3 = LogicalEval('01=1/10|1/&')
    print("01=1/10|1/&: " + logical_evaluator_trail_3.Process_Expression(), file = log)

    logical_evaluator_trail_4 = LogicalEval('11=0/0!&1|')
    print("11=0/0!&1|: " + logical_evaluator_trail_4.Process_Expression(), file = log)

    logical_evaluator_trail_5 = LogicalEval('10&11!&|0/')
    print("10&11!&|0/: " + logical_evaluator_trail_5.Process_Expression(), file = log)