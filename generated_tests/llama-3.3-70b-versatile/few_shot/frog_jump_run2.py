class TestCanCross(unittest.TestCase):
    def test_can_cross(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        result = can_cross(stones)
        self.assertTrue(result)

    def test_cannot_cross(self):
        stones = [0, 1, 2, 3, 4, 8, 9, 10]
        result = can_cross(stones)
        self.assertFalse(result)

    def test_empty_stones(self):
        stones = []
        result = can_cross(stones)
        self.assertFalse(result)

    def test_single_stone(self):
        stones = [0]
        result = can_cross(stones)
        self.assertTrue(result)

    def test_two_stones(self):
        stones = [0, 1]
        result = can_cross(stones)
        self.assertTrue(result)

    def test_large_gap(self):
        stones = [0, 10, 20, 30]
        result = can_cross(stones)
        self.assertFalse(result)