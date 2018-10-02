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

    def test_pop_one_element(self):
        # Arrange
        expecteditem = 5

        # Act
        self.postfixcalculator.push(5)
        actualitem = self.postfixcalculator.pop()

        # Assert
        self.assertEquals(expecteditem, actualitem)



if __name__ == '__main__':
        unittest.main()