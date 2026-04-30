class TestGeneratePascalsTriangle:
    def test_normal_input(self):
        assert generate_pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    def test_single_row(self):
        assert generate_pascals_triangle(1) == [[1]]

    def test_empty_input(self):
        assert generate_pascals_triangle(0) == []

    def test_zero_input(self):
        assert generate_pascals_triangle(0) == []

    def test_negative_input(self):
        try:
            generate_pascals_triangle(-1)
            assert False, "Expected ValueError for negative input"
        except ValueError:
            pass

    def test_non_integer_input(self):
        try:
            generate_pascals_triangle(3.5)
            assert False, "Expected TypeError for non-integer input"
        except TypeError:
            pass

    def test_large_input(self):
        assert len(generate_pascals_triangle(10)) == 10

    def test_invalid_input_type(self):
        try:
            generate_pascals_triangle("five")
            assert False, "Expected TypeError for invalid input type"
        except TypeError:
            pass

    def test_none_input(self):
        try:
            generate_pascals_triangle(None)
            assert False, "Expected TypeError for None input"
        except TypeError:
            pass