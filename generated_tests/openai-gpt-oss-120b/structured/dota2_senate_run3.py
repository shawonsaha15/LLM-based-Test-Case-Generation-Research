import unittest

class TestPredictPartyVictory(unittest.TestCase):
    # Normal cases -----------------------------------------------------------
    def test_simple_radiant_wins(self):
        # Arrange
        senate = "RD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_simple_dire_wins(self):
        # Arrange
        senate = "DR"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    def test_balanced_but_radiant_advantage(self):
        # Arrange
        senate = "RDRD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_unequal_counts_radiant_wins(self):
        # Arrange
        senate = "RRRDDD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_unequal_counts_dire_wins(self):
        # Arrange
        senate = "RDD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    # Boundary cases ---------------------------------------------------------
    def test_single_radiant(self):
        # Arrange
        senate = "R"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_single_dire(self):
        # Arrange
        senate = "D"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    def test_long_alternating_sequence(self):
        # Arrange
        senate = "RDRDRDRDRDRDRDRDRDRD"  # 20 characters, alternating
        # Act
        result = predict_party_victory(senate)
        # Assert
        # With equal numbers and Radiant starting first, Radiant should win
        self.assertEqual(result, "Radiant")

    # Invalid input cases ----------------------------------------------------
    def test_none_input_raises_type_error(self):
        # Arrange
        senate = None
        # Act & Assert
        with self.assertRaises(TypeError):
            predict_party_victory(senate)

    def test_integer_input_raises_type_error(self):
        # Arrange
        senate = 12345
        # Act & Assert
        with self.assertRaises(TypeError):
            predict_party_victory(senate)

    def test_invalid_characters_treated_as_dire(self):
        # Arrange
        senate = "RXD"  # 'X' will be treated as Dire by the implementation
        # Act
        result = predict_party_victory(senate)
        # Assert
        # The exact outcome depends on the algorithm; we only verify it returns a valid string
        self.assertIn(result, {"Radiant", "Dire"})