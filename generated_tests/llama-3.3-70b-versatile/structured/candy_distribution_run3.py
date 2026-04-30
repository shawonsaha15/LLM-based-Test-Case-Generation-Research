class TestCandyDistribution(unittest.TestCase):

    def test_normal_case(self):
        # Arrange
        ratings = [1, 0, 2]
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 5)

    def test_boundary_case_empty_list(self):
        # Arrange
        ratings = []
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 0)

    def test_boundary_case_single_element(self):
        # Arrange
        ratings = [1]
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 1)

    def test_boundary_case_two_elements(self):
        # Arrange
        ratings = [1, 2]
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 3)

    def test_invalid_input_none(self):
        # Arrange
        ratings = None
        
        # Act and Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_invalid_input_non_list(self):
        # Arrange
        ratings = 1
        
        # Act and Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_invalid_input_list_with_non_int(self):
        # Arrange
        ratings = [1, 'a']
        
        # Act and Assert
        with self.assertRaises(TypeError):
            candy_distribution(ratings)

    def test_large_input(self):
        # Arrange
        ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 55)

    def test_decreasing_ratings(self):
        # Arrange
        ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 55)

    def test_constant_ratings(self):
        # Arrange
        ratings = [5, 5, 5, 5, 5]
        
        # Act
        result = candy_distribution(ratings)
        
        # Assert
        self.assertEqual(result, 5)