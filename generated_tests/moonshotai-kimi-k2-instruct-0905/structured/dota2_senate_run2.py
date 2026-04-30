import unittest

class TestPredictPartyVictory(unittest.TestCase):

    # Normal Cases

    def test_radiant_wins_single_r(self):
        # Arrange
        senate = "R"
        expected = "Radiant"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_dire_wins_single_d(self):
        # Arrange
        senate = "D"
        expected = "Dire"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_radiant_wins_rr_dd(self):
        # Arrange
        senate = "RRDD"
        expected = "Radiant"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_dire_wins_dd_rr(self):
        # Arrange
        senate = "DDRR"
        expected = "Dire"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_radiant_wins_rdr(self):
        # Arrange
        senate = "RDR"
        expected = "Radiant"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_dire_wins_drd(self):
        # Arrange
        senate = "DRD"
        expected = "Dire"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    # Boundary Cases

    def test_all_radiant(self):
        # Arrange
        senate = "RRRRR"
        expected = "Radiant"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_all_dire(self):
        # Arrange
        senate = "DDDDD"
        expected = "Dire"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_alternating_rd_long(self):
        # Arrange
        senate = "RDRDRDRDRD"
        expected = "Radiant"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_alternating_dr_long(self):
        # Arrange
        senate = "DRDRDRDRDR"
        expected = "Dire"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_radiant_majority(self):
        # Arrange
        senate = "RRRDDDRR"
        expected = "Radiant"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    def test_dire_majority(self):
        # Arrange
        senate = "DDRRRRDD"
        expected = "Dire"
        # Act
        result = predict_party_victory(senate)
        # Assert
        self.assertEqual(result, expected)

    # Invalid Inputs (if applicable)

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

    def test_mixed_invalid_characters(self):
        # Arrange
        senate = "RDRDXD"
        # Act & Assert
        with self.assertRaises(KeyError):
            predict_party_victory(senate)