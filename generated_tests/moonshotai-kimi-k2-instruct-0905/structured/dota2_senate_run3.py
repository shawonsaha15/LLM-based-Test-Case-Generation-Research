import unittest


class TestPredictPartyVictory(unittest.TestCase):

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

    def test_radiant_majority(self):
        # Arrange
        senate = "RRDD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_dire_majority(self):
        # Arrange
        senate = "DDRR"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    def test_alternating_radiant_wins(self):
        # Arrange
        senate = "RD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_alternating_dire_wins(self):
        # Arrange
        senate = "DR"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    def test_large_radiant_first(self):
        # Arrange
        senate = "RRRRDDDD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_large_dire_first(self):
        # Arrange
        senate = "DDDDRRRR"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    def test_all_radiant(self):
        # Arrange
        senate = "RRRRR"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Radiant")

    def test_all_dire(self):
        # Arrange
        senate = "DDDDD"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, "Dire")

    def test_empty_string(self):
        # Arrange
        senate = ""
        # Act & Assert
        with self.assertRaises(IndexError):
            predict_party_victory(senate)

    def test_invalid_character(self):
        # Arrange
        senate = "RXD"
        # Act & Assert
        with self.assertRaises(KeyError):
            predict_party_victory(senate)