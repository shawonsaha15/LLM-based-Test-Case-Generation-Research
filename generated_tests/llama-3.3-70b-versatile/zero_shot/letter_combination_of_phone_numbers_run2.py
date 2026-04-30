class TestLetterCombinations(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_multiple_digits(self):
        expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(letter_combinations("23"), expected_output)

    def test_long_input(self):
        expected_output = ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", 
                           "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", 
                           "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
        self.assertEqual(letter_combinations("234"), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(KeyError):
            letter_combinations("01")