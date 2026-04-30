import unittest


class TestCandyDistribution(unittest.TestCase):

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
        ratings = [1, 3, 2, 2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 7)

    def test_boundary_single_element(self):
        # Arrange
        ratings = [5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 1)

    def test_boundary_two_equal(self):
        # Arrange
        ratings = [3, 3]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 2)

    def test_boundary_two_ascending(self):
        # Arrange
        ratings = [2, 5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    def test_boundary_two_descending(self):
        # Arrange
        ratings = [5, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)

    def test_boundary_all_equal(self):
        # Arrange
        ratings = [4, 4, 4, 4]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 4)

    def test_invalid_empty_list(self):
        # Arrange
        ratings = []
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 0)

    def test_normal_peak_in_middle(self):
        # Arrange
        ratings = [1, 2, 5, 3, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 11)

    def test_normal_valley_in_middle(self):
        # Arrange
        ratings = [3, 2, 1, 2, 3]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 13)

    def test_boundary_large_equal(self):
        # Arrange
        ratings = [10] * 100
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 100)

    def test_boundary_alternating_high_low(self):
        # Arrange
        ratings = [5, 1, 5, 1, 5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 9)