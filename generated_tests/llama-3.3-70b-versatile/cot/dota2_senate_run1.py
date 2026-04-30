class TestPredictPartyVictory:
    def test_radiant_wins(self):
        assert predict_party_victory("RRRR") == "Radiant"

    def test_dire_wins(self):
        assert predict_party_victory("DDDD") == "Dire"

    def test_empty_string(self):
        assert predict_party_victory("") == "Radiant"

    def test_single_radiant(self):
        assert predict_party_victory("R") == "Radiant"

    def test_single_dire(self):
        assert predict_party_victory("D") == "Dire"

    def test_balanced(self):
        assert predict_party_victory("RDDRRDD") == "Radiant"

    def test_radiant_wins_with_bans(self):
        assert predict_party_victory("RRDRDR") == "Radiant"

    def test_dire_wins_with_bans(self):
        assert predict_party_victory("DRDRDR") == "Dire"

    def test_invalid_input(self):
        try:
            predict_party_victory("Invalid")
            assert False, "Expected ValueError"
        except ValueError:
            assert True

    def test_long_string(self):
        long_string = "R" * 1000 + "D" * 999
        assert predict_party_victory(long_string) == "Radiant"

    def test_none_input(self):
        try:
            predict_party_victory(None)
            assert False, "Expected TypeError"
        except TypeError:
            assert True

    def test_large_input(self):
        large_string = "R" * 10000 + "D" * 9999
        assert predict_party_victory(large_string) == "Radiant"