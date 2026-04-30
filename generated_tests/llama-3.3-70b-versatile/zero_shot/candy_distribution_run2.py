class TestCandyDistribution(unittest.TestCase):
    def test_empty_ratings(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_rating(self):
        self.assertEqual(candy_distribution([1]), 1)

    def test_two_ratings_equal(self):
        self.assertEqual(candy_distribution([1, 1]), 2)

    def test_two_ratings_unequal(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_multiple_ratings_increasing(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4, 5]), 15)

    def test_multiple_ratings_decreasing(self):
        self.assertEqual(candy_distribution([5, 4, 3, 2, 1]), 15)

    def test_multiple_ratings_mixed(self):
        self.assertEqual(candy_distribution([1, 2, 3, 2, 1]), 9)

    def test_large_input(self):
        ratings = [1] * 100
        self.assertEqual(candy_distribution(ratings), 100)