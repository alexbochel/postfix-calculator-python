import unittest
from PostFixProject import LogicalEval

class TestLogicalEval(unittest.TestCase):

    def setUP(self):
        self.dummy = 0

    def test_equals_true(self):
        # Arrange
        logical_evaluator = LogicalEval('1=1')
        expected_char = '1'

        # Act
        actual_char = logical_evaluator.Process_Expression()

        # Assert
        self.assertEquals(expected_char, actual_char)



if __name__ == '__main__':
        unittest.main()