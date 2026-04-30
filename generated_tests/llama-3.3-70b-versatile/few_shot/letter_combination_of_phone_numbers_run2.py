class TestLetterCombinations(unittest.TestCase):
    def test_single_digit(self):
        result = letter_combinations("2")
        expected = ["a", "b", "c"]
        self.assertEqual(result, expected)

    def test_multiple_digits(self):
        result = letter_combinations("23")
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = letter_combinations("")
        expected = []
        self.assertEqual(result, expected)

    def test_invalid_digits(self):
        result = letter_combinations("01")
        expected = []
        self.assertEqual(result, expected)

    def test_long_input(self):
        result = letter_combinations("234")
        expected = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]
        self.assertEqual(result, expected)