import unittest
from PostFixProject import PostFixCalculator

class TestPostFixCalculator(unittest.TestCase):

    def setUp(self):
        self.postfixcalculator = PostFixCalculator()

    def test_push_first_item(self):
        # Arrange
        expecteditem = 5

        #Act
        self.postfixcalculator.push(5)

        # Assert
        self.assertEquals(self.postfixcalculator.stack[0], expecteditem)



if __name__ == '__main__':
        unittest.main()