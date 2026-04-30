import unittest

class TestCandyDistribution(unittest.TestCase):

    # Normal Cases
    def test_normal_ascending(self):
        # Arrange
        ratings = [1, 2, 3, 4, 5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 15)

    def test_normal_descending(self):
        # Arrange
        ratings = [5, 4, 3, 2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 15)

    def test_normal_mixed(self):
        # Arrange
        ratings = [1, 0, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 5)

    def test_normal_all_equal(self):
        # Arrange
        ratings = [3, 3, 3]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    # Boundary Cases
    def test_boundary_single_element(self):
        # Arrange
        ratings = [5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 1)

    def test_boundary_two_elements_ascending(self):
        # Arrange
        ratings = [1, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    def test_boundary_two_elements_descending(self):
        # Arrange
        ratings = [2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    def test_boundary_two_elements_equal(self):
        # Arrange
        ratings = [2, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 2)

    # Invalid Inputs
    def test_invalid_empty_list(self):
        # Arrange
        ratings = []
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 0)

    def test_invalid_large_peak(self):
        # Arrange
        ratings = [1, 3, 2, 2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 7)