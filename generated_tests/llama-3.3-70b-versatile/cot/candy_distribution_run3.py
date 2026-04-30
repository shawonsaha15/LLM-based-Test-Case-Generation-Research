class TestCandyDistribution:
    def test_empty_list(self):
        assert candy_distribution([]) == 0

    def test_single_element_list(self):
        assert candy_distribution([1]) == 1

    def test_increasing_ratings(self):
        assert candy_distribution([1, 2, 3, 4, 5]) == 15

    def test_decreasing_ratings(self):
        assert candy_distribution([5, 4, 3, 2, 1]) == 15

    def test_constant_ratings(self):
        assert candy_distribution([1, 1, 1, 1, 1]) == 5

    def test_large_ratings(self):
        assert candy_distribution([1000, 2000, 3000, 4000, 5000]) == 15

    def test_zero_ratings(self):
        assert candy_distribution([0, 0, 0, 0, 0]) == 5

    def test_negative_ratings(self):
        assert candy_distribution([-1, -2, -3, -4, -5]) == 15

    def test_mixed_ratings(self):
        assert candy_distribution([1, 3, 2, 4, 3]) == 9

    def test_invalid_input_none(self):
        try:
            candy_distribution(None)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_non_list(self):
        try:
            candy_distribution("12345")
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_list_with_non_int(self):
        try:
            candy_distribution([1, 2, "3", 4, 5])
            assert False, "Expected TypeError"
        except TypeError:
            pass