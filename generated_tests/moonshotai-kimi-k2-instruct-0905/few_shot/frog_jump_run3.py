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

    def test_three_stones_possible(self):
        result = can_cross([0, 1, 3])
        self.assertTrue(result)

    def test_three_stones_impossible(self):
        result = can_cross([0, 1, 4])
        self.assertFalse(result)

    def test_four_stones_possible(self):
        result = can_cross([0, 1, 3, 6])
        self.assertTrue(result)

    def test_four_stones_impossible(self):
        result = can_cross([0, 1, 2, 6])
        self.assertFalse(result)

    def test_large_gap_in_middle(self):
        result = can_cross([0, 1, 2, 3, 10])
        self.assertFalse(result)

    def test_consecutive_stones(self):
        result = can_cross([0, 1, 2, 3, 4, 5])
        self.assertTrue(result)

    def test_empty_list(self):
        result = can_cross([])
        self.assertFalse(result)