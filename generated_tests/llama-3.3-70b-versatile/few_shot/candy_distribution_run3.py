class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        result = candy_distribution([])
        self.assertEqual(result, 0)

    def test_single_element_list(self):
        result = candy_distribution([1])
        self.assertEqual(result, 1)

    def test_increasing_ratings(self):
        result = candy_distribution([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    def test_decreasing_ratings(self):
        result = candy_distribution([5, 4, 3, 2, 1])
        self.assertEqual(result, 15)

    def test_constant_ratings(self):
        result = candy_distribution([1, 1, 1, 1, 1])
        self.assertEqual(result, 5)

    def test_mixed_ratings(self):
        result = candy_distribution([1, 3, 2, 4, 5])
        self.assertEqual(result, 11)

    def test_large_list(self):
        ratings = [i % 10 + 1 for i in range(100)]
        result = candy_distribution(ratings)
        self.assertGreater(result, 0)