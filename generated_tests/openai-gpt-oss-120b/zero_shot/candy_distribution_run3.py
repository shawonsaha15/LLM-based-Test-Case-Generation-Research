import unittest

class TestCandyDistribution(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(candy_distribution([]), 0)

    def test_single_element(self):
        self.assertEqual(candy_distribution([10]), 1)

    def test_all_equal(self):
        self.assertEqual(candy_distribution([4, 4, 4, 4]), 4)

    def test_strictly_increasing(self):
        # 1,2,3,4 -> candies 1+2+3+4 = 10
        self.assertEqual(candy_distribution([1, 2, 3, 4]), 10)

    def test_strictly_decreasing(self):
        # 5,4,3,2,1 -> candies 5+4+3+2+1 = 15
        self.assertEqual(candy_distribution([5, 4, 3, 2, 1]), 15)

    def test_plateau(self):
        # 1,2,2 -> candies 1,2,1 = 4
        self.assertEqual(candy_distribution([1, 2, 2]), 4)

    def test_typical_example(self):
        # 1,0,2 -> candies 2,1,2 = 5
        self.assertEqual(candy_distribution([1, 0, 2]), 5)

    def test_complex_case(self):
        # 1,3,4,5,2 -> expected 11
        # left  = [1,2,3,4,1]
        # right = [1,1,2,1,1]
        # max   = [1,2,3,4,1] sum = 11
        self.assertEqual(candy_distribution([1, 3, 4, 5, 2]), 11)

    def test_alternating(self):
        # 1,3,2,2,1 -> expected 7
        # left  = [1,2,1,1,1]
        # right = [1,2,1,1,1]
        # max   = [1,2,1,1,1] sum = 6? Actually compute manually:
        # ratings: 1<3>2=2>1
        # candies: 1,2,1,2,1 = 7
        self.assertEqual(candy_distribution([1, 3, 2, 2, 1]), 7)