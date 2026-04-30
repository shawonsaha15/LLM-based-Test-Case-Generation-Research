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

class TestLetter_combinations(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])
        self.assertEqual(letter_combinations("9"), ["w", "x", "y", "z"])

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertEqual(letter_combinations("23"), expected)

    def test_invalid_digits(self):
        self.assertEqual(letter_combinations("1"), [])
        self.assertEqual(letter_combinations("0"), [])
        self.assertEqual(letter_combinations("*#"), [])
        self.assertEqual(letter_combinations("2*"), ["a", "b", "c"])

    def test_mixed_valid_invalid(self):
        # '1' yields no letters, so overall result should be empty
        self.assertEqual(letter_combinations("21"), [])
        # '0' yields no letters, overall result empty
        self.assertEqual(letter_combinations("20"), [])

    def test_three_digits_length(self):
        result = letter_combinations("234")
        self.assertEqual(len(result), 27)
        # Verify first and last elements to ensure ordering
        self.assertEqual(result[0], "adg")
        self.assertEqual(result[-1], "cfi")

    def test_four_digits_combination_count(self):
        result = letter_combinations("279")
        self.assertEqual(len(result), 3 * 4 * 4)  # 48 combinations

if __name__ == "__main__":
    unittest.main()