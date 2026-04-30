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

    def test_two_stones_successful(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_two_stones_unreachable(self):
        stones = [0, 2]
        self.assertFalse(can_cross(stones))

    def test_consecutive_stones(self):
        stones = list(range(0, 11))  # 0 through 10
        self.assertTrue(can_cross(stones))

    def test_large_gap_unreachable(self):
        stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 70]
        # The jump from 55 to 70 requires a 15‑unit jump, which is impossible
        self.assertFalse(can_cross(stones))

    def test_complex_reachable_pattern(self):
        stones = [0, 1, 2, 5, 6, 9, 12, 13, 16, 19, 22]
        # This pattern can be crossed by varying jumps of 1, 2, and 3 units
        self.assertTrue(can_cross(stones))