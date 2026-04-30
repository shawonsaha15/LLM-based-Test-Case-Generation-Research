class TestPredictPartyVictory:
    def test_normal_input(self):
        assert predict_party_victory("RRRR") == "Radiant"
        assert predict_party_victory("DDDD") == "Dire"
        assert predict_party_victory("RRDD") == "Radiant"

    def test_empty_input(self):
        assert predict_party_victory("") == "Radiant"

    def test_single_input(self):
        assert predict_party_victory("R") == "Radiant"
        assert predict_party_victory("D") == "Dire"

    def test_large_input(self):
        assert predict_party_victory("R" * 1000) == "Radiant"
        assert predict_party_victory("D" * 1000) == "Dire"

    def test_invalid_input(self):
        try:
            predict_party_victory(None)
            assert False
        except TypeError:
            assert True

        try:
            predict_party_victory(123)
            assert False
        except TypeError:
            assert True

        try:
            predict_party_victory("RDX")
            assert False
        except AssertionError:
            assert True

    def test_edge_cases(self):
        assert predict_party_victory("RDRD") == "Radiant"
        assert predict_party_victory("DRDR") == "Dire"
        assert predict_party_victory("RRDR") == "Radiant"
        assert predict_party_victory("DDRD") == "Dire"