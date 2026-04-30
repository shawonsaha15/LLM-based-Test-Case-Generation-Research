class TestPredictPartyVictory:
    def test_normal_case_radiant_wins(self):
        # Arrange
        senate = "RRR"

        # Act
        result = predict_party_victory(senate)

        # Assert
        assert result == "Radiant"

    def test_normal_case_dire_wins(self):
        # Arrange
        senate = "DDD"

        # Act
        result = predict_party_victory(senate)

        # Assert
        assert result == "Dire"

    def test_boundary_case_radiant_wins(self):
        # Arrange
        senate = "RR"

        # Act
        result = predict_party_victory(senate)

        # Assert
        assert result == "Radiant"

    def test_boundary_case_dire_wins(self):
        # Arrange
        senate = "DD"

        # Act
        result = predict_party_victory(senate)

        # Assert
        assert result == "Dire"

    def test_invalid_input_empty_string(self):
        # Arrange
        senate = ""

        # Act and Assert
        assert predict_party_victory(senate) == "Radiant"  # This may fail depending on the implementation

    def test_invalid_input_none(self):
        # Arrange
        senate = None

        # Act and Assert
        try:
            predict_party_victory(senate)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_non_string(self):
        # Arrange
        senate = 123

        # Act and Assert
        try:
            predict_party_victory(senate)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_string_with_invalid_characters(self):
        # Arrange
        senate = "ABC"

        # Act and Assert
        result = predict_party_victory(senate)
        assert result in ["Radiant", "Dire"]  # This may fail depending on the implementation

    def test_radiant_wins_with_bans(self):
        # Arrange
        senate = "RDRD"

        # Act
        result = predict_party_victory(senate)

        # Assert
        assert result == "Radiant"

    def test_dire_wins_with_bans(self):
        # Arrange
        senate = "DRDR"

        # Act
        result = predict_party_victory(senate)

        # Assert
        assert result == "Dire"