import sys

class PostFixCalculator:

    def __init__(self):
        self.PF1 = "0!!!1/10&1!!&=1=0|"
        self.PF2 = "10=!10/&11!0/=1|11!&|&0/"
        self.stack = list()
        self.index = 0

    def push(self, element):
        self.stack.append(element)
        self.index += 1

    def pop(self):
        return -1

    def solve_postfix(self, first, second, operator):



        return -1


# Get this part working. TODO
def Main(argv):
    calculator = PostFixCalculator(argv)

if __name__ == "__main__":
    Main(sys.argv[1:])