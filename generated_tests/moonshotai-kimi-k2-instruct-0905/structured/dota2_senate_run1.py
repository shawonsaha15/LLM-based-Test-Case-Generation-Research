import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_normal_radiant_wins(self):
        # Arrange
        senate = "RRDD"
        expected = "Radiant"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_normal_dire_wins(self):
        # Arrange
        senate = "DDRR"
        expected = "Dire"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_normal_alternating_radiant_wins(self):
        # Arrange
        senate = "RD"
        expected = "Radiant"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_normal_alternating_dire_wins(self):
        # Arrange
        senate = "DR"
        expected = "Dire"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_single_radiant(self):
        # Arrange
        senate = "R"
        expected = "Radiant"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_single_dire(self):
        # Arrange
        senate = "D"
        expected = "Dire"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_all_radiant(self):
        # Arrange
        senate = "RRRRR"
        expected = "Radiant"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_boundary_all_dire(self):
        # Arrange
        senate = "DDDDD"
        expected = "Dire"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_normal_longer_radiant_wins(self):
        # Arrange
        senate = "RRRDDDRR"
        expected = "Radiant"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)

    def test_normal_longer_dire_wins(self):
        # Arrange
        senate = "DDRRRRDD"
        expected = "Dire"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        self.assertEqual(result, expected)