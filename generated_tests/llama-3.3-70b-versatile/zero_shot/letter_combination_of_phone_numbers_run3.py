class TestLetterCombinations(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_multiple_digits(self):
        expected_result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(letter_combinations("23"), expected_result)

    def test_invalid_digit(self):
        self.assertEqual(letter_combinations("10"), [])

    def test_multiple_invalid_digits(self):
        self.assertEqual(letter_combinations("101"), [])

    def test_long_input(self):
        result = letter_combinations("234")
        self.assertEqual(len(result), 27)