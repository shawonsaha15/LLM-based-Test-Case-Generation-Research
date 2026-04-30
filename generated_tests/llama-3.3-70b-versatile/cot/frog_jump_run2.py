class TestCanCross:
    def test_normal_input(self):
        assert can_cross([0, 1, 3, 5, 6, 8, 12, 17]) == True

    def test_empty_input(self):
        assert can_cross([]) == False

    def test_single_stone(self):
        assert can_cross([0]) == False

    def test_two_stones(self):
        assert can_cross([0, 1]) == True

    def test_large_values(self):
        assert can_cross([0, 1000, 2000, 3000]) == True

    def test_zero_jumps(self):
        assert can_cross([0, 0, 0]) == False

    def test_negative_jumps(self):
        try:
            can_cross([-1, 0, 1])
            assert False, "Expected ValueError or False"
        except ValueError:
            pass

    def test_invalid_input_type(self):
        try:
            can_cross("123")
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_input_values(self):
        try:
            can_cross([None, 1, 2])
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_unreachable_stones(self):
        assert can_cross([0, 100, 200, 300]) == False