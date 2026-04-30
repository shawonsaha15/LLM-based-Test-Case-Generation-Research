class TestCandyDistribution(unittest.TestCase):
    def test_empty_ratings(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_rating(self):
        self.assertEqual(candy_distribution([1]), 1)

    def test_two_ratings_equal(self):
        self.assertEqual(candy_distribution([1, 1]), 2)

    def test_two_ratings_ascending(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_two_ratings_descending(self):
        self.assertEqual(candy_distribution([2, 1]), 3)

    def test_multiple_ratings_ascending(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 6)

    def test_multiple_ratings_descending(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 6)

    def test_multiple_ratings_mixed(self):
        self.assertEqual(candy_distribution([1, 2, 1, 2, 1]), 9)

    def test_large_input(self):
        ratings = [1] * 100
        self.assertEqual(candy_distribution(ratings), 100)