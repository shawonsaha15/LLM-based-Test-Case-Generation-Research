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
    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_two_digits(self):
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertEqual(letter_combinations("23"), expected)

    def test_multiple_digits(self):
        expected = [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]
        self.assertEqual(letter_combinations("79"), expected)

    def test_invalid_digit(self):
        self.assertEqual(letter_combinations("1"), [])

    def test_mixed_invalid(self):
        self.assertEqual(letter_combinations("2a3"), [])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            letter_combinations(None)

if __name__ == "__main__":
    unittest.main()