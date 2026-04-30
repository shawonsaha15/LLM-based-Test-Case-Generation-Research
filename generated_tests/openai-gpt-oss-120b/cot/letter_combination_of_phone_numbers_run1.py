import unittest
import itertools

class TestLetterCombinations(unittest.TestCase):
    digit_map = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    def expected_combinations(self, digits: str):
        """Helper to compute the expected combinations using the same mapping."""
        if not digits:
            return []
        pools = [self.digit_map.get(d, "") for d in digits]
        # If any digit maps to an empty string, the product is empty.
        if any(p == "" for p in pools):
            return []
        return [''.join(p) for p in itertools.product(*pools)]

    def test_empty_input(self):
        self.assertEqual(letter_combinations(""), [])

    def test_single_digit(self):
        for digit, letters in self.digit_map.items():
            with self.subTest(digit=digit):
                expected = list(letters)
                self.assertCountEqual(letter_combinations(digit), expected)
                # order should match the mapping order
                self.assertEqual(letter_combinations(digit), expected)

    def test_two_digits_example(self):
        digits = "23"
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        self.assertEqual(letter_combinations(digits), expected)

    def test_invalid_digits_return_empty(self):
        for invalid in ["1", "0", "*", "a", ""]:
            with self.subTest(invalid=invalid):
                # Single invalid character should yield empty list
                self.assertEqual(letter_combinations(invalid), [])
        # Mixed valid/invalid should also yield empty because an invalid digit produces no letters
        self.assertEqual(letter_combinations("2a3"), [])
        self.assertEqual(letter_combinations("2*3"), [])

    def test_multiple_digits_correct_count_and_content(self):
        digits = "2345"
        result = letter_combinations(digits)
        expected = self.expected_combinations(digits)
        # Verify count matches product of possible letters per digit
        self.assertEqual(len(result), len(expected))
        # Verify every element is a string of correct length
        for combo in result:
            self.assertIsInstance(combo, str)
            self.assertEqual(len(combo), len(digits))
        # Verify content matches expected set (order is also checked)
        self.assertCountEqual(result, expected)
        self.assertEqual(result, expected)  # order should be deterministic

    def test_large_input_performance_and_correctness(self):
        digits = "279"
        result = letter_combinations(digits)
        expected = self.expected_combinations(digits)
        self.assertEqual(result, expected)

    def test_input_immutability(self):
        digits = "23"
        original = digits[:]
        _ = letter_combinations(digits)
        self.assertEqual(digits, original)  # strings are immutable; ensure not altered

    def test_no_extra_characters_in_output(self):
        digits = "79"
        result = letter_combinations(digits)
        allowed = set(self.digit_map['7'] + self.digit_map['9'])
        for combo in result:
            for ch in combo:
                self.assertIn(ch, allowed)