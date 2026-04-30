class TestCanCrossFunction(unittest.TestCase):
    def test_base_case(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        self.assertTrue(can_cross(stones))

    def test_cannot_cross(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 10]
        self.assertFalse(can_cross(stones))

    def test_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_two_stones(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_large_gap(self):
        stones = [0, 1, 100]
        self.assertFalse(can_cross(stones))

    def test_empty_list(self):
        stones = []
        with self.assertRaises(IndexError):
            can_cross(stones)