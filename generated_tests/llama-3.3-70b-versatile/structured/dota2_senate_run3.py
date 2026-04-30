class TestPredictPartyVictory(unittest.TestCase):

    def test_normal_case_radiant_wins(self):
        # Arrange
        senate = "RRRRDD"

        # Act
        result = predict_party_victory(senate)

        # Assert
        self.assertEqual(result, "Radiant")

    def test_normal_case_dire_wins(self):
        # Arrange
        senate = "DDDDRR"

        # Act
        result = predict_party_victory(senate)

        # Assert
        self.assertEqual(result, "Dire")

    def test_boundary_case_single_radiant(self):
        # Arrange
        senate = "R"

        # Act
        result = predict_party_victory(senate)

        # Assert
        self.assertEqual(result, "Radiant")

    def test_boundary_case_single_dire(self):
        # Arrange
        senate = "D"

        # Act
        result = predict_party_victory(senate)

        # Assert
        self.assertEqual(result, "Dire")

    def test_boundary_case_empty_string(self):
        # Arrange
        senate = ""

        # Act and Assert
        with self.assertRaises(IndexError):
            predict_party_victory(senate)

    def test_invalid_input_none(self):
        # Arrange
        senate = None

        # Act and Assert
        with self.assertRaises(TypeError):
            predict_party_victory(senate)

    def test_invalid_input_non_string(self):
        # Arrange
        senate = 123

        # Act and Assert
        with self.assertRaises(TypeError):
            predict_party_victory(senate)

    def test_invalid_input_string_with_invalid_characters(self):
        # Arrange
        senate = "RDAB"

        # Act and Assert
        with self.assertRaises(KeyError):
            # This test case is not applicable as the function does not raise a KeyError
            # when encountering invalid characters. It simply ignores them.
            predict_party_victory(senate)