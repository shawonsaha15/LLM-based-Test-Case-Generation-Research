import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        expected = ["a", "b", "c"]
        self.assertListEqual(letter_combinations("2"), expected)

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertListEqual(letter_combinations("23"), expected)

    def test_invalid_digit(self):
        # Digits '0' and '1' have no mapping, resulting in no combinations
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])
        self.assertEqual(letter_combinations("210"), [])

    def test_three_digits(self):
        # "7" maps to 4 letters, "9" maps to 4 letters, total combos = 4*4 = 16
        result = letter_combinations("79")
        expected = [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]
        self.assertListEqual(result, expected)

    def test_longer_input(self):
        # Verify length of result for a 3‑digit input
        result = letter_combinations("234")
        # 3 letters * 3 letters * 3 letters = 27 combinations
        self.assertEqual(len(result), 27)
        # Spot‑check a few expected combinations
        self.assertIn("adg", result)
        self.assertIn("cfi", result)
        self.assertIn("beh", result)