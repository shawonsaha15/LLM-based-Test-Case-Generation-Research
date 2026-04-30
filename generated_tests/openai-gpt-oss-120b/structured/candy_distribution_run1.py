import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_normal_cases(self):
        # Arrange
        ratings_cases = [
            ([1, 0, 2], 5),          # classic example
            ([1, 2, 2], 4),          # plateau at the end
            ([4, 3, 2, 1], 10),      # strictly decreasing
            ([1, 2, 3, 4], 10),      # strictly increasing
            ([1, 3, 4, 5, 2], 11),   # peak in the middle
        ]

        for ratings, expected in ratings_cases:
            with self.subTest(ratings=ratings):
                # Act
                result = candy_distribution(ratings)

                # Assert
                self.assertEqual(result, expected)

    def test_boundary_cases(self):
        # Arrange & Act & Assert for single element
        self.assertEqual(candy_distribution([5]), 1)

        # Arrange & Act & Assert for two elements
        self.assertEqual(candy_distribution([1, 2]), 3)   # 1,2
        self.assertEqual(candy_distribution([2, 1]), 3)   # 2,1

        # Empty list (already handled in function)
        self.assertEqual(candy_distribution([]), 0)

        # Large uniform list (all equal)
        uniform = [7] * 100
        self.assertEqual(candy_distribution(uniform), 100)

        # Long increasing then decreasing
        inc_dec = list(range(1, 51)) + list(range(50, 0, -1))
        # The expected total can be derived: sum of 1..50 + sum of 1..49 + 50 (peak counted once)
        expected = sum(range(1, 51)) + sum(range(1, 50))
        self.assertEqual(candy_distribution(inc_dec), expected)

    def test_invalid_inputs(self):
        # Non‑list input
        with self.assertRaises(TypeError):
            candy_distribution(None)

        with self.assertRaises(TypeError):
            candy_distribution("invalid")

        # List with non‑int elements
        with self.assertRaises(TypeError):
            candy_distribution([1, "a", 3])

        # List containing None
        with self.assertRaises(TypeError):
            candy_distribution([1, None, 2])