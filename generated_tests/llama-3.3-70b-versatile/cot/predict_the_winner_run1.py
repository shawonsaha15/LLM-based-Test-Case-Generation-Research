class TestPredictTheWinner:
    def test_normal_input(self):
        assert predict_the_winner([1, 5, 233, 7]) == True

    def test_empty_input(self):
        assert predict_the_winner([]) == True

    def test_single_element_input(self):
        assert predict_the_winner([5]) == True

    def test_two_elements_input(self):
        assert predict_the_winner([1, 2]) == True

    def test_large_input(self):
        assert predict_the_winner([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True

    def test_zero_input(self):
        assert predict_the_winner([0, 0, 0]) == True

    def test_negative_input(self):
        assert predict_the_winner([-1, -2, -3]) == False

    def test_mixed_input(self):
        assert predict_the_winner([-1, 2, -3, 4]) == True

    def test_invalid_input(self):
        try:
            predict_the_winner(None)
            assert False, "Expected ValueError to be raised"
        except ValueError:
            pass

    def test_invalid_input_type(self):
        try:
            predict_the_winner("123")
            assert False, "Expected TypeError to be raised"
        except TypeError:
            pass

    def test_invalid_input_list_type(self):
        try:
            predict_the_winner([1, "2", 3])
            assert False, "Expected TypeError to be raised"
        except TypeError:
            pass