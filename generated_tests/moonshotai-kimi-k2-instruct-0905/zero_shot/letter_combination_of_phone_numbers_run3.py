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
        expected = sorted(["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
                           "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
                           "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"])
        self.assertEqual(sorted(letter_combinations("234")), expected)

    def test_digit_with_four_letters(self):
        self.assertEqual(sorted(letter_combinations("7")), sorted(["p", "q", "r", "s"]))
        self.assertEqual(sorted(letter_combinations("9")), sorted(["w", "x", "y", "z"]))

    def test_mixed_digits(self):
        result = letter_combinations("29")
        expected = sorted(["aw", "ax", "ay", "az", "bw", "bx", "by", "bz", "cw", "cx", "cy", "cz"])
        self.assertEqual(sorted(result), expected)

    def test_invalid_digit(self):
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])
        self.assertEqual(letter_combinations("20"), [])

    def test_long_input(self):
        result = letter_combinations("2345")
        self.assertEqual(len(result), 3 * 3 * 3 * 3)
        self.assertIn("adgj", result)
        self.assertIn("cfil", result)