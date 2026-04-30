import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(sorted(letter_combinations("2")), sorted(["a", "b", "c"]))
        self.assertEqual(sorted(letter_combinations("3")), sorted(["d", "e", "f"]))
        self.assertEqual(sorted(letter_combinations("7")), sorted(["p", "q", "r", "s"]))

    def test_two_digits(self):
        self.assertEqual(sorted(letter_combinations("23")), sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]))

    def test_three_digits(self):
        self.assertEqual(sorted(letter_combinations("234")), sorted([
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]))

    def test_digit_with_four_letters(self):
        self.assertEqual(sorted(letter_combinations("7")), sorted(["p", "q", "r", "s"]))
        self.assertEqual(sorted(letter_combinations("9")), sorted(["w", "x", "y", "z"]))

    def test_invalid_digit(self):
        self.assertEqual(letter_combinations("01"), [])

    def test_repeated_digits(self):
        self.assertEqual(sorted(letter_combinations("22")), sorted([
            "aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"
        ]))