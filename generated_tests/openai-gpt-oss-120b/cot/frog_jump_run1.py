import unittest

class TestCanCross(unittest.TestCase):
    def test_single_stone_returns_true(self):
        # Only the starting stone; already at the last stone.
        self.assertTrue(can_cross([0]))

    def test_basic_true_example(self):
        # Classic example where the frog can cross.
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_basic_false_example(self):
        # Example where the frog cannot reach the last stone.
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        self.assertFalse(can_cross(stones))

    def test_all_consecutive_stones(self):
        # Every unit distance; the frog can always make a jump of +1.
        stones = list(range(0, 10))  # [0,1,2,...,9]
        self.assertTrue(can_cross(stones))

    def test_initial_jump_too_big(self):
        # The second stone is too far for the initial jump of length 1.
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_none_input_raises_type_error(self):
        # Passing None should raise a TypeError when len() is called.
        with self.assertRaises(TypeError):
            can_cross(None)

    def test_non_integer_elements_raise_type_error(self):
        # Elements that are not integers should cause a TypeError during subtraction.
        with self.assertRaises(TypeError):
            can_cross([0, 'a', 2])

    def test_large_number_of_consecutive_stones(self):
        # Stress test with many stones; should still be reachable.
        stones = list(range(0, 101))  # 0 through 100 inclusive
        self.assertTrue(can_cross(stones))

    def test_unreachable_due_to_gap_even_with_large_n(self):
        # Large gap that cannot be bridged despite the number of stones.
        stones = [0, 1, 2, 3, 4, 5, 15, 16, 17]
        self.assertFalse(can_cross(stones))

    def test_duplicate_stone_positions(self):
        # Duplicate positions should not affect the ability to cross.
        stones = [0, 0, 1, 2, 3]
        self.assertTrue(can_cross(stones))