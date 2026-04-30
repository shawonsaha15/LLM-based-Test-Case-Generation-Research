import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty(self):
        # Arrange
        ratings = []
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 0)

    def test_single_child(self):
        # Arrange
        ratings = [5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 1)

    def test_increasing_ratings(self):
        # Arrange
        ratings = [1, 2, 3, 4, 5]
        # Act
        result = candy_distribution(ratings)
        # Assert
        # Each child gets one more candy than the previous: 1+2+3+4+5 = 15
        self.assertEqual(result, 15)

    def test_decreasing_ratings(self):
        # Arrange
        ratings = [5, 4, 3, 2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        # Same as increasing but from the right side: 5+4+3+2+1 = 15
        self.assertEqual(result, 15)

    def test_plateau_ratings(self):
        # Arrange
        ratings = [2, 2, 2, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        # No child needs more than 1 candy: 4 * 1 = 4
        self.assertEqual(result, 4)

    def test_mixed_ratings(self):
        # Arrange
        ratings = [1, 0, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        # Expected distribution: [2, 1, 2] => total 5
        self.assertEqual(result, 5)

    def test_complex_mixed_ratings(self):
        # Arrange
        ratings = [1, 3, 4, 5, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        # Expected distribution: [1, 2, 3, 4, 1] => total 11
        self.assertEqual(result, 11)

    def test_boundary_two_children_increasing(self):
        # Arrange
        ratings = [1, 2]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)  # 1 + 2

    def test_boundary_two_children_decreasing(self):
        # Arrange
        ratings = [2, 1]
        # Act
        result = candy_distribution(ratings)
        # Assert
        self.assertEqual(result, 3)  # 2 + 1

    def test_invalid_none_input(self):
        # Arrange
        ratings = None
        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_invalid_nonlist_input(self):
        # Arrange
        ratings = "invalid"
        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_invalid_nonint_elements(self):
        # Arrange
        ratings = [1, "a", 3]
        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)