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
    def test_empty(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_two_digits(self):
        self.assertEqual(
            letter_combinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        )

    def test_digit_with_four_letters(self):
        expected = [a + b for a in "pqrs" for b in "wxyz"]
        self.assertEqual(letter_combinations("79"), expected)

    def test_invalid_digit(self):
        self.assertEqual(letter_combinations("1"), [])

    def test_mixed_valid_invalid(self):
        self.assertEqual(letter_combinations("21"), [])

if __name__ == "__main__":
    unittest.main()