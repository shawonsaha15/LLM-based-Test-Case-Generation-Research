import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_normal_cases(self):
        # Arrange
        cases = [
            ("RD", "Radiant"),
            ("DR", "Dire"),
            ("RRDD", "Radiant"),
            ("DDRR", "Dire"),
            ("RDRD", "Radiant"),
            ("DRDR", "Dire"),
            ("RRRDDD", "Radiant"),
            ("DDDRRR", "Dire"),
        ]
        for senate, expected in cases:
            with self.subTest(senate=senate):
                # Act
                result = predict_party_victory(senate)
                # Assert
                self.assertEqual(result, expected)

    def test_boundary_cases(self):
        # Single senator cases (minimum non‑empty input)
        single_cases = [
            ("R", "Radiant"),
            ("D", "Dire"),
        ]
        for senate, expected in single_cases:
            with self.subTest(senate=senate):
                # Act
                result = predict_party_victory(senate)
                # Assert
                self.assertEqual(result, expected)

        # Long alternating pattern
        long_alternating = "RDRDRDRDRDRD"
        # Expected winner can be deduced: Radiant will win because the first R bans the following D,
        # and the pattern repeats, leaving only Radiant senators active.
        with self.subTest(senate=long_alternating):
            result = predict_party_victory(long_alternating)
            self.assertEqual(result, "Radiant")

    def test_invalid_inputs(self):
        # Non‑standard characters are treated as Dire (else branch)
        invalid_char_cases = [
            ("rD", "Dire"),
            ("XRRD", "Radiant"),  # 'X' is treated as Dire, but Radiant outnumbers after bans
        ]
        for senate, expected in invalid_char_cases:
            with self.subTest(senate=senate):
                result = predict_party_victory(senate)
                self.assertEqual(result, expected)

        # Non‑string iterable (list of characters)
        with self.subTest(senate=['R', 'D', 'R']):
            result = predict_party_victory(['R', 'D', 'R'])
            self.assertEqual(result, "Radiant")

        # None input should raise a TypeError because len(None) is invalid
        with self.subTest(senate=None):
            with self.assertRaises(TypeError):
                predict_party_victory(None)

        # Empty string would cause an infinite loop; ensure it raises an exception quickly.
        # The implementation does not guard against this, so we expect it to raise an IndexError
        # after the loop attempts to access an empty active set.
        with self.subTest(senate=""):
            with self.assertRaises(Exception):
                predict_party_victory("")