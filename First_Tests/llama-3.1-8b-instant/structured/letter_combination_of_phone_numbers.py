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
    def test_normal_cases(self):
        self.assertEqual(letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(letter_combinations("4"), ["g", "h", "i"])
        self.assertEqual(letter_combinations("9"), ["w", "x", "y", "z"])

    def test_edge_cases(self):
        self.assertEqual(letter_combinations(""), [])
        self.assertEqual(letter_combinations("1"), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            letter_combinations(123)
        with self.assertRaises(TypeError):
            letter_combinations("abc")

if __name__ == "__main__":
    unittest.main()