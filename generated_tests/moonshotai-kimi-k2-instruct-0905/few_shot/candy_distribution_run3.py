class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        result = candy_distribution([])
        self.assertEqual(result, 0)

    def test_single_child(self):
        result = candy_distribution([5])
        self.assertEqual(result, 1)

    def test_all_equal_ratings(self):
        result = candy_distribution([3, 3, 3])
        self.assertEqual(result, 3)

    def test_increasing_ratings(self):
        result = candy_distribution([1, 2, 3, 4])
        self.assertEqual(result, 10)

    def test_decreasing_ratings(self):
        result = candy_distribution([4, 3, 2, 1])
        self.assertEqual(result, 10)

    def test_peak_in_middle(self):
        result = candy_distribution([1, 3, 2, 1])
        self.assertEqual(result, 7)

    def test_valley_in_middle(self):
        result = candy_distribution([3, 2, 1, 2, 3])
        self.assertEqual(result, 11)

    def test_two_children_equal(self):
        result = candy_distribution([5, 5])
        self.assertEqual(result, 2)

    def test_large_peak(self):
        result = candy_distribution([1, 2, 5, 3, 2])
        self.assertEqual(result, 9)

    def test_alternating_high_low(self):
        result = candy_distribution([1, 5, 1, 5, 1])
        self.assertEqual(result, 9)