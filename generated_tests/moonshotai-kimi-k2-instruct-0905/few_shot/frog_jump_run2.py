class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        result = can_cross([0])
        self.assertTrue(result)

    def test_two_stones_adjacent(self):
        result = can_cross([0, 1])
        self.assertTrue(result)

    def test_two_stones_not_adjacent(self):
        result = can_cross([0, 2])
        self.assertFalse(result)

    def test_three_stones_crossable(self):
        result = can_cross([0, 1, 3])
        self.assertTrue(result)

    def test_three_stones_not_crossable(self):
        result = can_cross([0, 2, 5])
        self.assertFalse(result)

    def test_empty_list(self):
        result = can_cross([])
        self.assertFalse(result)

    def test_large_gap_early(self):
        result = can_cross([0, 1, 2, 3, 4, 8, 9, 11])
        self.assertFalse(result)

    def test_crossable_with_increasing_steps(self):
        result = can_cross([0, 1, 3, 6, 10])
        self.assertTrue(result)

    def test_not_crossable_with_big_gap(self):
        result = can_cross([0, 1, 2, 3, 4, 6, 9, 15])
        self.assertFalse(result)

    def test_crossable_with_varied_steps(self):
        result = can_cross([0, 1, 2, 5, 7, 9, 10])
        self.assertTrue(result)