class TestPredictPartyVictory:
    def test_normal_input(self):
        assert predict_party_victory("RRR") == "Radiant"
        assert predict_party_victory("DDD") == "Dire"
        assert predict_party_victory("RDD") == "Dire"
        assert predict_party_victory("DDR") == "Radiant"

    def test_empty_input(self):
        with pytest.raises(IndexError):
            predict_party_victory("")

    def test_single_input(self):
        assert predict_party_victory("R") == "Radiant"
        assert predict_party_victory("D") == "Dire"

    def test_large_input(self):
        assert predict_party_victory("R" * 1000) == "Radiant"
        assert predict_party_victory("D" * 1000) == "Dire"

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            predict_party_victory(123)

    def test_invalid_characters(self):
        with pytest.raises(AssertionError):
            predict_party_victory("RXD")

    def test_tied_input(self):
        with pytest.raises(AssertionError):
            predict_party_victory("RD")

    def test_ban_count(self):
        assert predict_party_victory("RRDR") == "Radiant"
        assert predict_party_victory("DDRD") == "Dire"