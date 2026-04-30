class TestCanCross(unittest.TestCase):
    def test_single_stone(self):
        result = can_cross([0])
        self.assertTrue(result)

    def test_two_stones(self):
        result = can_cross([0, 1])
        self.assertTrue(result)

    def test_three_stones(self):
        result = can_cross([0, 1, 3])
        self.assertTrue(result)

    def test_four_stones(self):
        result = can_cross([0, 1, 3, 5, 6, 8, 12, 17])
        self.assertTrue(result)

    def test_five_stones(self):
        result = can_cross([0, 1, 2, 3, 4, 8, 9, 11])
        self.assertFalse(result)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            can_cross([])

    def test_large_stones(self):
        result = can_cross([0, 1000000])
        self.assertFalse(result)

    def test_negative_stones(self):
        with self.assertRaises(ValueError):
            can_cross([-1, 0, 1])

    def test_non_integer_stones(self):
        with self.assertRaises(TypeError):
            can_cross([0, 1.5, 3])