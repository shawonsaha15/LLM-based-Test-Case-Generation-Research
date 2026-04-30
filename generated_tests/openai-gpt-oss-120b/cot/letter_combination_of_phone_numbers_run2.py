import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        expected = ["a", "b", "c"]
        self.assertCountEqual(letter_combinations("2"), expected)

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertCountEqual(letter_combinations("23"), expected)

    def test_multiple_digits(self):
        # 4 digits, each maps to 3 letters => 81 combinations
        result = letter_combinations("2345")
        self.assertEqual(len(result), 81)
        # Spot‑check a few expected combinations
        self.assertIn("adgj", result)
        self.assertIn("cfil", result)
        self.assertIn("behk", result)

    def test_digit_with_no_mapping(self):
        # Digits 0 and 1 have no letters; any presence should yield no combinations
        self.assertEqual(letter_combinations("10"), [])
        self.assertEqual(letter_combinations("203"), [])
        self.assertEqual(letter_combinations("001"), [])

    def test_non_digit_characters(self):
        # Characters not in the map behave like missing letters
        self.assertEqual(letter_combinations("2a3"), [])
        self.assertEqual(letter_combinations("b"), [])

    def test_invalid_type_none(self):
        with self.assertRaises(TypeError):
            letter_combinations(None)

    def test_invalid_type_int(self):
        with self.assertRaises(TypeError):
            letter_combinations(23)

    def test_large_combination_count(self):
        # 7 maps to 4 letters, 9 maps to 4 letters => 16 combos
        result = letter_combinations("79")
        self.assertEqual(len(result), 16)
        expected = [
            a + b
            for a in "pqrs"
            for b in "wxyz"
        ]
        self.assertCountEqual(result, expected)