class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        result = can_cross([0])
        self.assertTrue(result)

    def test_two_stones(self):
        result = can_cross([0, 1])
        self.assertTrue(result)

    def test_multiple_stones_can_cross(self):
        result = can_cross([0, 1, 3, 5, 6, 8, 12, 17])
        self.assertTrue(result)

    def test_multiple_stones_cannot_cross(self):
        result = can_cross([0, 1, 2, 3, 4, 8, 9, 10])
        self.assertFalse(result)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            can_cross([])

    def test_stones_with_negative_values(self):
        with self.assertRaises(ValueError):
            can_cross([-1, 0, 1])

    def test_stones_with_duplicates(self):
        result = can_cross([0, 0, 1])
        self.assertTrue(result)