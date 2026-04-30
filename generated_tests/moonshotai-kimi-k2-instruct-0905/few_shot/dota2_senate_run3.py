class TestPredictPartyVictory(unittest.TestCase):
    def test_radiant_wins(self):
        result = predict_party_victory("RRDD")
        self.assertEqual(result, "Radiant")

    def test_dire_wins(self):
        result = predict_party_victory("DDRR")
        self.assertEqual(result, "Dire")

    def test_radiant_wins_majority(self):
        result = predict_party_victory("RRRDDD")
        self.assertEqual(result, "Radiant")

    def test_dire_wins_majority(self):
        result = predict_party_victory("DDDRRR")
        self.assertEqual(result, "Dire")

    def test_single_radiant(self):
        result = predict_party_victory("R")
        self.assertEqual(result, "Radiant")

    def test_single_dire(self):
        result = predict_party_victory("D")
        self.assertEqual(result, "Dire")

    def test_alternating_parties_radiant_wins(self):
        result = predict_party_victory("RD")
        self.assertEqual(result, "Radiant")

    def test_alternating_parties_dire_wins(self):
        result = predict_party_victory("DR")
        self.assertEqual(result, "Dire")

    def test_longer_radiant_streak(self):
        result = predict_party_victory("RRRDDDRR")
        self.assertEqual(result, "Radiant")

    def test_longer_dire_streak(self):
        result = predict_party_victory("DDRRRRDD")
        self.assertEqual(result, "Dire")