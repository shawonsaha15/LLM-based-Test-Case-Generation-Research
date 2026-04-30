import unittest

class TestCandyDistribution(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_child(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_two_equal_ratings(self):
        self.assertEqual(candy_distribution([3, 3]), 2)

    def test_two_increasing_ratings(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_two_decreasing_ratings(self):
        self.assertEqual(candy_distribution([2, 1]), 3)

    def test_general_case(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_all_equal_ratings(self):
        self.assertEqual(candy_distribution([4, 4, 4, 4]), 4)

    def test_ascending_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4, 5]), 15)

    def test_descending_ratings(self):
        self.assertEqual(candy_distribution([5, 4, 3, 2, 1]), 15)

    def test_mixed_ratings(self):
        self.assertEqual(candy_distribution([1, 3, 2, 2, 1]), 7)