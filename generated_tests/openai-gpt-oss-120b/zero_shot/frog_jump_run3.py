import unittest

class TestCanCross(unittest.TestCase):
    def test_example_true(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_example_false(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones_impossible(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_two_stones_possible(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_triangular_numbers(self):
        # Jumps increase by 1 each time: 1,2,3,4,...
        stones = [0, 1, 3, 6, 10, 15, 21, 28]
        self.assertTrue(can_cross(stones))

    def test_large_gap_blocked(self):
        stones = [0, 1, 2, 3, 4, 5, 6, 20]
        self.assertFalse(can_cross(stones))

    def test_alternate_possible_path(self):
        stones = [0, 1, 3, 4, 5, 7, 9, 10, 12]
        self.assertTrue(can_cross(stones))

    def test_no_initial_jump(self):
        # First jump must be 1, but the second stone is farther away
        stones = [0, 2, 3, 4, 5]
        self.assertFalse(can_cross(stones))

    def test_complex_true_case(self):
        stones = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12, 16, 21, 27, 34]
        self.assertTrue(can_cross(stones))

    def test_complex_false_case(self):
        stones = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12, 16, 21, 27, 35]
        self.assertFalse(can_cross(stones))