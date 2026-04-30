class TestPredictPartyVictory:
    def test_normal_case_radiant_wins(self):
        # Arrange
        senate = "RRRDDD"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        assert result == "Radiant"

    def test_normal_case_dire_wins(self):
        # Arrange
        senate = "DDDDRR"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        assert result == "Dire"

    def test_boundary_case_single_radiant(self):
        # Arrange
        senate = "R"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        assert result == "Radiant"

    def test_boundary_case_single_dire(self):
        # Arrange
        senate = "D"
        
        # Act
        result = predict_party_victory(senate)
        
        # Assert
        assert result == "Dire"

    def test_invalid_input_empty_string(self):
        # Arrange
        senate = ""
        
        # Act and Assert
        with assertRaises(ValueError):
            predict_party_victory(senate)

    def test_invalid_input_non_string_input(self):
        # Arrange
        senate = 123
        
        # Act and Assert
        with assertRaises(TypeError):
            predict_party_victory(senate)

    def test_invalid_input_non_RD_characters(self):
        # Arrange
        senate = "RDAB"
        
        # Act and Assert
        with assertRaises(ValueError):
            predict_party_victory(senate)