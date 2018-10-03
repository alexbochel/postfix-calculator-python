import unittest
from PostFixProject import Stack

class TestPostFixCalculator(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_first_item(self):
        # Arrange
        expected_item = 5

        #Act
        self.stack.Push(5)

        # Assert
        self.assertEquals(self.stack.stack[0], expected_item)

    def test_pop_one_element(self):
        # Arrange
        expected_item = 5

        # Act
        self.stack.Push(5)
        actual_item = self.stack.Pop()

        # Assert
        self.assertEquals(expected_item, actual_item)

    def test_push_and_pop_multiple_elements(self):
        # Arrange
        expected_item_1 = 1
        expected_item_2 = 2
        expected_item_3 = 3
        expected_item_4 = 4
        expected_item_5 = 5

        # Act
        self.stack.Push(expected_item_1)
        self.stack.Push(expected_item_2)
        self.stack.Push(expected_item_3)
        self.stack.Push(expected_item_4)
        self.stack.Push(expected_item_5)

        actual_item_1 = self.stack.Pop()
        actual_item_2 = self.stack.Pop()
        actual_item_3 = self.stack.Pop()
        actual_item_4 = self.stack.Pop()
        actual_item_5 = self.stack.Pop()

        # Assert
        self.assertEquals(expected_item_1, actual_item_5)
        self.assertEquals(expected_item_2, actual_item_4)
        self.assertEquals(expected_item_3, actual_item_3)
        self.assertEquals(expected_item_4, actual_item_2)
        self.assertEquals(expected_item_5, actual_item_1)

if __name__ == '__main__':
        unittest.main()