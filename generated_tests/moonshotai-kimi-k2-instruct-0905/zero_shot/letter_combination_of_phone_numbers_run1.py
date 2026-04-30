import unittest

class TestLetterCombinations(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(sorted(letter_combinations("2")), ["a", "b", "c"])
        self.assertEqual(sorted(letter_combinations("3")), ["d", "e", "f"])
        self.assertEqual(sorted(letter_combinations("4")), ["g", "h", "i"])
        self.assertEqual(sorted(letter_combinations("5")), ["j", "k", "l"])
        self.assertEqual(sorted(letter_combinations("6")), ["m", "n", "o"])
        self.assertEqual(sorted(letter_combinations("7")), ["p", "q", "r", "s"])
        self.assertEqual(sorted(letter_combinations("8")), ["t", "u", "v"])
        self.assertEqual(sorted(letter_combinations("9")), ["w", "x", "y", "z"])

    def test_two_digits(self):
        self.assertEqual(
            sorted(letter_combinations("23")),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        )

    def test_three_digits(self):
        self.assertEqual(
            sorted(letter_combinations("234")),
            sorted([
                "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
                "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
                "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
            ])
        )

    def test_with_invalid_digit(self):
        self.assertEqual(letter_combinations("01"), [])

    def test_mixed_valid_invalid(self):
        self.assertEqual(letter_combinations("2#3"), [])

    def test_repeated_digits(self):
        self.assertEqual(
            sorted(letter_combinations("22")),
            ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        )