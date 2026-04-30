class TestCandyDistribution(unittest.TestCase):
    def test_empty_ratings(self):
        result = candy_distribution([])
        self.assertEqual(result, 0)

    def test_single_child(self):
        result = candy_distribution([1])
        self.assertEqual(result, 1)

    def test_two_children_equal_ratings(self):
        result = candy_distribution([1, 1])
        self.assertEqual(result, 2)

    def test_two_children_unequal_ratings(self):
        result = candy_distribution([1, 2])
        self.assertEqual(result, 3)

    def test_multiple_children_ascending_ratings(self):
        result = candy_distribution([1, 2, 3])
        self.assertEqual(result, 6)

    def test_multiple_children_descending_ratings(self):
        result = candy_distribution([3, 2, 1])
        self.assertEqual(result, 6)

    def test_multiple_children_oscillating_ratings(self):
        result = candy_distribution([1, 3, 2, 4, 3])
        self.assertEqual(result, 11)