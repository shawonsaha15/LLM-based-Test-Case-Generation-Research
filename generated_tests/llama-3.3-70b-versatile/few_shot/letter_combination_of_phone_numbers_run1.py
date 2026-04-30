class TestLetterCombinations(unittest.TestCase):
    def test_empty_string(self):
        result = letter_combinations("")
        self.assertEqual(result, [])

    def test_single_digit(self):
        result = letter_combinations("2")
        self.assertEqual(result, ["a", "b", "c"])

    def test_multiple_digits(self):
        result = letter_combinations("23")
        self.assertEqual(result, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_invalid_digits(self):
        result = letter_combinations("01")
        self.assertEqual(result, [])

    def test_long_digits(self):
        result = letter_combinations("234")
        self.assertEqual(len(result), 3 * 3 * 4)

    def test_only_valid_digits(self):
        result = letter_combinations("789")
        self.assertEqual(len(result), 4 * 3 * 4)