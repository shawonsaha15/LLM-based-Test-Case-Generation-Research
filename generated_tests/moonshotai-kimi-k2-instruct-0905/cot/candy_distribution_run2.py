import unittest

class TestCandyDistribution(unittest.TestCase):

    def test_normal_case_ascending(self):
        self.assertEqual(candy_distribution([1, 2, 3]), 6)

    def test_normal_case_descending(self):
        self.assertEqual(candy_distribution([3, 2, 1]), 6)

    def test_normal_case_mixed(self):
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_normal_case_equal_ratings(self):
        self.assertEqual(candy_distribution([1, 1, 1]), 3)

    def test_normal_case_single_peak(self):
        self.assertEqual(candy_distribution([1, 3, 2, 1]), 7)

    def test_normal_case_single_valley(self):
        self.assertEqual(candy_distribution([3, 1, 2, 3]), 7)

    def test_edge_case_empty_list(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(candy_distribution([5]), 1)

    def test_edge_case_two_equal(self):
        self.assertEqual(candy_distribution([2, 2]), 2)

    def test_edge_case_two_ascending(self):
        self.assertEqual(candy_distribution([1, 2]), 3)

    def test_edge_case_two_descending(self):
        self.assertEqual(candy_distribution([2, 1]), 3)

    def test_edge_case_large_values(self):
        ratings = [1000000, 2000000, 3000000]
        self.assertEqual(candy_distribution(ratings), 6)

    def test_edge_case_all_zeros(self):
        self.assertEqual(candy_distribution([0, 0, 0]), 3)

    def test_edge_case_negative_ratings(self):
        self.assertEqual(candy_distribution([-1, -2, -3]), 6)

    def test_edge_case_mixed_negative_positive(self):
        self.assertEqual(candy_distribution([-1, 0, 1]), 5)

    def test_edge_case_large_input_size(self):
        ratings = [i % 3 for i in range(1000)]
        result = candy_distribution(ratings)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            candy_distribution(None)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            candy_distribution("not a list")

    def test_invalid_input_dict(self):
        with self.assertRaises(TypeError):
            candy_distribution({"a": 1})

    def test_invalid_input_list_with_strings(self):
        with self.assertRaises(TypeError):
            candy_distribution([1, "two", 3])

    def test_mutant_fault_left_array_not_updated(self):
        # Simulate mutant where left[i] is not updated correctly
        # Expected correct behavior should still pass
        ratings = [1, 2, 3, 2, 1]
        self.assertEqual(candy_distribution(ratings), 9)

    def test_mutant_fault_right_array_not_updated(self):
        # Simulate mutant where right[i] is not updated correctly
        # Expected correct behavior should still pass
        ratings = [3, 2, 1, 2, 3]
        self.assertEqual(candy_distribution(ratings), 9)

    def test_mutant_fault_total_not_max_of_left_right(self):
        # Simulate mutant where total uses min instead of max
        # Expected correct behavior should still pass
        ratings = [1, 2, 1]
        self.assertEqual(candy_distribution(ratings), 4)

    def test_mutant_fault_initial_values_not_one(self):
        # Simulate mutant where left/right arrays are initialized to 0
        # Expected correct behavior should still pass
        ratings = [1, 2, 3]
        self.assertEqual(candy_distribution(ratings), 6)