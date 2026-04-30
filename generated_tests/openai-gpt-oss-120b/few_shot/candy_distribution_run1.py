import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_all_equal_ratings(self):
        ratings = [3, 3, 3, 3]
        self.assertEqual(candy_distribution(ratings), len(ratings))

    def test_strictly_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        n = len(ratings)
        expected = n * (n + 1) // 2  # 1+2+3+...+n
        self.assertEqual(candy_distribution(ratings), expected)

    def test_strictly_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        n = len(ratings)
        expected = n * (n + 1) // 2  # same as increasing case
        self.assertEqual(candy_distribution(ratings), expected)

    def test_mixed_ratings_example1(self):
        # Classic example from the candy problem
        ratings = [1, 0, 2]
        # Expected distribution: [2, 1, 2] => total 5
        self.assertEqual(candy_distribution(ratings), 5)

    def test_mixed_ratings_example2(self):
        ratings = [1, 2, 2]
        # Expected distribution: [1, 2, 1] => total 4
        self.assertEqual(candy_distribution(ratings), 4)

    def test_plateau_middle(self):
        ratings = [1, 2, 2, 1]
        # Expected distribution: [1, 2, 2, 1] => total 6
        self.assertEqual(candy_distribution(ratings), 6)

    def test_complex_pattern(self):
        ratings = [1, 3, 4, 5, 2]
        # Left pass:  [1,2,3,4,1]
        # Right pass: [1,1,2,3,1]
        # Max per child: [1,2,3,4,1] => total 11
        self.assertEqual(candy_distribution(ratings), 11)

    def test_long_random_like(self):
        ratings = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
        # Computed expected total manually or via known solution:
        # Distribution should be [1,2,1,2,1,2,3,4,2,1] => sum = 19
        self.assertEqual(candy_distribution(ratings), 19)