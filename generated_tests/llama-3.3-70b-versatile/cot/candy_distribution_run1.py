class TestCandyDistribution(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element_list(self):
        self.assertEqual(candy_distribution([1]), 1)

    def test_two_elements_list_with_equal_ratings(self):
        self.assertEqual(candy_distribution([1, 1]), 2)

    def test_two_elements_list_with_unequal_ratings(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_large_list_with_unequal_ratings(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_list_with_all_equal_ratings(self):
        self.assertEqual(candy_distribution([1, 1, 1, 1]), 4)

    def test_list_with_increasing_ratings(self):
        self.assertEqual(candy_distribution([1, 2, 3, 4]), 10)

    def test_list_with_decreasing_ratings(self):
        self.assertEqual(candy_distribution([4, 3, 2, 1]), 10)

    def test_list_with_alternating_ratings(self):
        self.assertEqual(candy_distribution([1, 3, 2, 4]), 7)

    def test_list_with_negative_ratings(self):
        self.assertEqual(candy_distribution([-1, -2, -3, -4]), 10)

    def test_list_with_zero_ratings(self):
        self.assertEqual(candy_distribution([0, 0, 0, 0]), 4)

    def test_list_with_large_ratings(self):
        self.assertEqual(candy_distribution([1000, 2000, 3000, 4000]), 10)