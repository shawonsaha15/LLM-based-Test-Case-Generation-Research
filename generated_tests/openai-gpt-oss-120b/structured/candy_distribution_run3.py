import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_ratings(self):
        # Arrange
        ratings = []
        expected = 0

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_single_child(self):
        # Arrange
        ratings = [5]
        expected = 1

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_two_children_increasing(self):
        # Arrange
        ratings = [1, 2]
        expected = 3  # 1 + 2

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_two_children_decreasing(self):
        # Arrange
        ratings = [2, 1]
        expected = 3  # 2 + 1

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_plateau(self):
        # Arrange
        ratings = [1, 1, 1]
        expected = 3  # each child gets 1

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_increasing_sequence(self):
        # Arrange
        ratings = [1, 2, 3, 4]
        expected = 10  # 1+2+3+4

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_decreasing_sequence(self):
        # Arrange
        ratings = [4, 3, 2, 1]
        expected = 10  # 4+3+2+1

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_mixed_ratings_example(self):
        # Arrange
        ratings = [1, 0, 2]
        expected = 5  # distribution: [2,1,2]

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_valley(self):
        # Arrange
        ratings = [2, 1, 2]
        expected = 5  # distribution: [2,1,2]

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)

    def test_invalid_input_none(self):
        # Arrange
        ratings = None

        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_invalid_input_non_int(self):
        # Arrange
        ratings = [1, "a", 2]

        # Act & Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_large_monotonic_increasing(self):
        # Arrange
        n = 1000
        ratings = list(range(1, n + 1))
        expected = n * (n + 1) // 2  # sum of 1..n

        # Act
        result = candy_distribution(ratings)

        # Assert
        self.assertEqual(result, expected)