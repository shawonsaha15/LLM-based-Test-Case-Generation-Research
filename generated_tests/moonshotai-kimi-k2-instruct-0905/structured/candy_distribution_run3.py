import unittest

class TestCandyDistribution(unittest.TestCase):

    # Normal cases
    def test_increasing_ratings(self):
        # Arrange
        ratings = [1, 2, 3, 4, 5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 15)

    def test_decreasing_ratings(self):
        # Arrange
        ratings = [5, 4, 3, 2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 15)

    def test_mixed_ratings(self):
        # Arrange
        ratings = [1, 3, 2, 2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 7)

    def test_all_equal_ratings(self):
        # Arrange
        ratings = [5, 5, 5, 5, 5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 5)

    def test_single_peak(self):
        # Arrange
        ratings = [1, 2, 5, 3, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 9)

    # Boundary cases
    def test_empty_list(self):
        # Arrange
        ratings = []
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 0)

    def test_single_element(self):
        # Arrange
        ratings = [10]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 1)

    def test_two_elements_increasing(self):
        # Arrange
        ratings = [1, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    def test_two_elements_decreasing(self):
        # Arrange
        ratings = [2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    def test_two_elements_equal(self):
        # Arrange
        ratings = [3, 3]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 2)

    # Invalid inputs (handled by function contract)
    def test_none_input(self):
        # Arrange
        ratings = None
        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_non_list_input(self):
        # Arrange
        ratings = "not a list"
        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_non_int_elements(self):
        # Arrange
        ratings = [1, 2.5, 3]
        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)