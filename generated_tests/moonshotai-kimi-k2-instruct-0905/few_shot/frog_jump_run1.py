class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        result = can_cross([0])
        self.assertTrue(result)

    def test_two_stones(self):
        result = can_cross([0, 1])
        self.assertTrue(result)

    def test_impossible_gap(self):
        result = can_cross([0, 2])
        self.assertFalse(result)

    def test_typical_crossable(self):
        result = can_cross([0, 1, 3, 5, 6, 8, 12, 17])
        self.assertTrue(result)

    def test_not_crossable(self):
        result = can_cross([0, 1, 2, 3, 4, 8, 9, 11])
        self.assertFalse(result)

    def test_large_gap_at_start(self):
        result = can_cross([0, 5])
        self.assertFalse(result)

    def test_three_stones_crossable(self):
        result = can_cross([0, 1, 3])
        self.assertTrue(result)

    def test_three_stones_not_crossable(self):
        result = can_cross([0, 1, 4])
        self.assertFalse(result)