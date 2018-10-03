import unittest
from PostFixProject import PostFixCalculator

class TestPostFixCalculator(unittest.TestCase):

    def setUp(self):
        self.post_fix_calculator = PostFixCalculator()

    def test_push_first_item(self):
        # Arrange
        expected_item = 5

        #Act
        self.post_fix_calculator.push(5)

        # Assert
        self.assertEquals(self.post_fix_calculator.stack[0], expected_item)

    def test_pop_one_element(self):
        # Arrange
        expected_item = 5

        # Act
        self.post_fix_calculator.push(5)
        actual_item = self.post_fix_calculator.pop()

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
        self.post_fix_calculator.push(expected_item_1)
        self.post_fix_calculator.push(expected_item_2)
        self.post_fix_calculator.push(expected_item_3)
        self.post_fix_calculator.push(expected_item_4)
        self.post_fix_calculator.push(expected_item_5)

        actual_item_1 = self.post_fix_calculator.pop()
        actual_item_2 = self.post_fix_calculator.pop()
        actual_item_3 = self.post_fix_calculator.pop()
        actual_item_4 = self.post_fix_calculator.pop()
        actual_item_5 = self.post_fix_calculator.pop()

        # Assert
        self.assertEquals(expected_item_1, actual_item_5)
        self.assertEquals(expected_item_2, actual_item_4)
        self.assertEquals(expected_item_3, actual_item_3)
        self.assertEquals(expected_item_4, actual_item_2)
        self.assertEquals(expected_item_5, actual_item_1)



if __name__ == '__main__':
        unittest.main()