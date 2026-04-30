def letter_combinations(digits: str) -> list[str]:
    digit_map = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    if not digits:
        return []

    result = []
    n = len(digits)

    def backtrack(index: int, path: str):
        if index == n:
            result.append(path)
            return

        letters = digit_map.get(digits[index], "")

        for letter in letters:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result

import unittest

class TestLetterCombinations(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_multiple_digits(self):
        self.assertEqual(letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_invalid_input(self):
        self.assertEqual(letter_combinations("01"), [])

    def test_invalid_input_with_letters(self):
        self.assertEqual(letter_combinations("2a"), [])

    def test_long_input(self):
        self.assertEqual(len(letter_combinations("234")), 27)

if __name__ == '__main__':
    unittest.main()