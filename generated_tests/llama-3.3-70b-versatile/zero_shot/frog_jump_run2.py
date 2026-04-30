class TestCanCrossFunction(unittest.TestCase):

    def test_can_cross_with_valid_stones(self):
        stones = [0,1,3,5,6,8,12,17]
        self.assertTrue(can_cross(stones))

    def test_can_cross_with_invalid_stones(self):
        stones = [0,1,2,3,4,8,9,10]
        self.assertFalse(can_cross(stones))

    def test_can_cross_with_empty_stones(self):
        stones = []
        with self.assertRaises(IndexError):
            can_cross(stones)

    def test_can_cross_with_single_stone(self):
        stones = [0]
        self.assertTrue(can_cross(stones))

    def test_can_cross_with_two_stones(self):
        stones = [0, 1]
        self.assertTrue(can_cross(stones))

    def test_can_cross_with_large_stones(self):
        stones = [0, 1000, 2000, 3000]
        self.assertTrue(can_cross(stones))