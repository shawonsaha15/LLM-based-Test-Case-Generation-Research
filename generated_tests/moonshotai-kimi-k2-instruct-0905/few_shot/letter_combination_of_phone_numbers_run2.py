class TestLetterCombinations(unittest.TestCase):
    def test_empty_string(self):
        result = letter_combinations("")
        self.assertEqual(result, [])

    def test_single_digit(self):
        result = letter_combinations("2")
        self.assertEqual(result, ["a", "b", "c"])

    def test_two_digits(self):
        result = letter_combinations("23")
        self.assertEqual(result, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_three_digits(self):
        result = letter_combinations("234")
        expected = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]
        self.assertEqual(result, expected)

    def test_digit_with_four_letters(self):
        result = letter_combinations("7")
        self.assertEqual(result, ["p", "q", "r", "s"])

    def test_digit_with_three_letters(self):
        result = letter_combinations("9")
        self.assertEqual(result, ["w", "x", "y", "z"])

    def test_invalid_digit(self):
        result = letter_combinations("01")
        self.assertEqual(result, [])

    def test_repeated_digits(self):
        result = letter_combinations("22")
        expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        self.assertEqual(result, expected)