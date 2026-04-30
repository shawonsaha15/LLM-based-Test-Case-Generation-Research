class TestPredictTheWinner(unittest.TestCase):

    def test_normal_case_even_length(self):
        # Arrange
        nums = [1, 5, 233, 7]
        
        # Act
        result = predict_the_winner(nums)
        
        # Assert
        self.assertTrue(result)

    def test_normal_case_odd_length(self):
        # Arrange
        nums = [1, 5, 2]
        
        # Act
        result = predict_the_winner(nums)
        
        # Assert
        self.assertTrue(result)

    def test_boundary_case_empty_list(self):
        # Arrange
        nums = []
        
        # Act
        with self.assertRaises(IndexError):
            predict_the_winner(nums)
        
        # Assert
        # No need for assert here as we are checking for exception

    def test_boundary_case_single_element(self):
        # Arrange
        nums = [1]
        
        # Act
        result = predict_the_winner(nums)
        
        # Assert
        self.assertTrue(result)

    def test_boundary_case_two_elements(self):
        # Arrange
        nums = [1, 2]
        
        # Act
        result = predict_the_winner(nums)
        
        # Assert
        self.assertTrue(result)

    def test_invalid_input_none(self):
        # Arrange
        nums = None
        
        # Act and Assert
        with self.assertRaises(TypeError):
            predict_the_winner(nums)

    def test_invalid_input_not_list(self):
        # Arrange
        nums = "123"
        
        # Act and Assert
        with self.assertRaises(TypeError):
            predict_the_winner(nums)

    def test_invalid_input_list_with_non_int(self):
        # Arrange
        nums = [1, '2', 3]
        
        # Act and Assert
        with self.assertRaises(TypeError):
            predict_the_winner(nums)