import unittest

class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        self.assertTrue(can_cross([0]))

    def test_two_stones(self):
        self.assertTrue(can_cross([0, 1]))

    def test_example_true(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_example_false(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_empty_raises(self):
        with self.assertRaises(IndexError):
            can_cross([])

    def test_non_start_zero(self):
        # First stone not at position 0 should be unreachable
        stones = [1, 2, 3, 4, 5]
        self.assertFalse(can_cross(stones))

    def test_unsorted_input(self):
        # Unsorted list should be treated as given; expected to be unreachable
        stones = [0, 2, 1, 3, 5]
        self.assertFalse(can_cross(stones))

    def test_large_sequence(self):
        # 200 stones spaced 1 unit apart – should be reachable
        stones = list(range(200))
        self.assertTrue(can_cross(stones))

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            can_cross(None)

    def test_max_jump_boundary(self):
        # n = 5, a jump of length 6 should be ignored (k > n)
        stones = [0, 1, 2, 3, 4, 10]  # distance from 4 to 10 is 6 > n (6 > 5)
        self.assertFalse(can_cross(stones))