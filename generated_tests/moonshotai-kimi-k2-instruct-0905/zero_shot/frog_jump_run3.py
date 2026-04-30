import unittest

class TestCanCross(unittest.TestCase):
    def test_empty_stones(self):
        self.assertFalse(can_cross([]))

    def test_single_stone(self):
        self.assertTrue(can_cross([0]))

    def test_two_stones(self):
        self.assertTrue(can_cross([0, 1]))

    def test_impossible_jump(self):
        self.assertFalse(can_cross([0, 2]))

    def test_simple_path(self):
        self.assertTrue(can_cross([0, 1, 3, 5]))

    def test_no_path(self):
        self.assertFalse(can_cross([0, 1, 2, 3, 4, 8, 9, 11]))

    def test_large_gap(self):
        self.assertFalse(can_cross([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))

    def test_complex_path(self):
        self.assertTrue(can_cross([0, 1, 3, 6, 10, 15, 16, 21]))

    def test_repeated_stones(self):
        self.assertFalse(can_cross([0, 1, 1, 2]))

    def test_reverse_order(self):
        self.assertFalse(can_cross([5, 4, 3, 2, 1, 0]))