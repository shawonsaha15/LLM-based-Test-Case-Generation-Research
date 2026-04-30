class TestCandyDistribution:
    def test_empty_ratings(self):
        assert candy_distribution([]) == 0

    def test_single_rating(self):
        assert candy_distribution([1]) == 1

    def test_two_ratings_equal(self):
        assert candy_distribution([1, 1]) == 2

    def test_two_ratings_unequal(self):
        assert candy_distribution([1, 2]) == 3

    def test_multiple_ratings(self):
        assert candy_distribution([1, 2, 2]) == 4
        assert candy_distribution([1, 0, 2]) == 5
        assert candy_distribution([1, 3, 2, 2, 1]) == 7

    def test_large_ratings(self):
        assert candy_distribution([1000, 2000, 3000]) == 6

    def test_negative_ratings(self):
        assert candy_distribution([-1, -2, -3]) == 6

    def test_zero_ratings(self):
        assert candy_distribution([0, 0, 0]) == 3

    def test_invalid_input_none(self):
        try:
            candy_distribution(None)
            assert False, "Expected TypeError"
        except TypeError:
            assert True

    def test_invalid_input_non_list(self):
        try:
            candy_distribution(123)
            assert False, "Expected TypeError"
        except TypeError:
            assert True

    def test_invalid_input_list_with_non_int(self):
        try:
            candy_distribution([1, 'a', 3])
            assert False, "Expected TypeError"
        except TypeError:
            assert True