import unittest

class TestPredictPartyVictory(unittest.TestCase):
    # Normal cases
    def test_normal_cases(self):
        # Arrange
        cases = [
            ("RD", "Radiant"),
            ("DR", "Dire"),
            ("RRDD", "Radiant"),
            ("RDRD", "Radiant"),
            ("RRRDDD", "Radiant"),
            ("DDRR", "Dire"),
        ]

        for senate, expected in cases:
            with self.subTest(senate=senate):
                # Act
                result = predict_party_victory(senate)

                # Assert
                self.assertEqual(result, expected)

    # Boundary cases
    def test_boundary_cases(self):
        # Arrange
        single_r = "R"
        single_d = "D"
        long_alternating = "RD" * 500  # 1000 characters

        # Act & Assert for single character strings
        self.assertEqual(predict_party_victory(single_r), "Radiant")
        self.assertEqual(predict_party_victory(single_d), "Dire")

        # Act & Assert for a long alternating string
        # The expected winner for an even length alternating string is Radiant
        self.assertEqual(predict_party_victory(long_alternating), "Radiant")

    # Invalid inputs
    def test_invalid_inputs(self):
        # Arrange
        non_string_input = None
        invalid_chars = "RXD"  # 'X' is not a valid party character

        # Act & Assert for non-string input (should raise a TypeError)
        with self.assertRaises(TypeError):
            predict_party_victory(non_string_input)

        # Act for string containing invalid characters
        # The implementation treats any character other than 'R' as 'D'
        result = predict_party_victory(invalid_chars)

        # Assert that the result is still one of the valid outputs
        self.assertIn(result, {"Radiant", "Dire"})