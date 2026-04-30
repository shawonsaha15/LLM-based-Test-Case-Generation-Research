class TestPredictTheWinner:
    def test_normal_input(self):
        assert predict_the_winner([1, 5, 2]) == True
        assert predict_the_winner([1, 5, 233, 7]) == True

    def test_empty_input(self):
        assert predict_the_winner([]) == True

    def test_single_element_input(self):
        assert predict_the_winner([5]) == True

    def test_two_element_input(self):
        assert predict_the_winner([1, 1]) == True
        assert predict_the_winner([1, 2]) == True
        assert predict_the_winner([2, 1]) == False

    def test_large_values_input(self):
        assert predict_the_winner([1000, 1000]) == True
        assert predict_the_winner([1000, 2000]) == True
        assert predict_the_winner([2000, 1000]) == False

    def test_negative_values_input(self):
        assert predict_the_winner([-1, -1]) == True
        assert predict_the_winner([-1, -2]) == True
        assert predict_the_winner([-2, -1]) == False

    def test_invalid_input(self):
        try:
            predict_the_winner(None)
            assert False, "Expected TypeError"
        except TypeError:
            pass

        try:
            predict_the_winner("123")
            assert False, "Expected TypeError"
        except TypeError:
            pass

        try:
            predict_the_winner([1, "2", 3])
            assert False, "Expected TypeError"
        except TypeError:
            pass