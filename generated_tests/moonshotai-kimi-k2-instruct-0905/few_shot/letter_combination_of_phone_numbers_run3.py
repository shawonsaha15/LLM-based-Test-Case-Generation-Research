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

    def test_digit_with_four_letters(self):
        result = letter_combinations("7")
        self.assertEqual(result, ["p", "q", "r", "s"])

    def test_invalid_digit(self):
        result = letter_combinations("1")
        self.assertEqual(result, [])

    def test_mixed_valid_invalid(self):
        result = letter_combinations("29")
        self.assertEqual(result, ["aw", "ax", "ay", "az", "bw", "bx", "by", "bz", "cw", "cx", "cy", "cz"])

    def test_longer_sequence(self):
        result = letter_combinations("234")
        self.assertEqual(len(result), 27)