class TestPredictPartyVictory(unittest.TestCase):
    def test_radiant_wins(self):
        result = predict_party_victory("RRDD")
        self.assertEqual(result, "Radiant")

    def test_dire_wins(self):
        result = predict_party_victory("DDRR")
        self.assertEqual(result, "Dire")

    def test_radiant_wins_longer(self):
        result = predict_party_victory("RRRDDD")
        self.assertEqual(result, "Radiant")

    def test_dire_wins_longer(self):
        result = predict_party_victory("DDDDRRR")
        self.assertEqual(result, "Dire")

    def test_all_radiant(self):
        result = predict_party_victory("RRRR")
        self.assertEqual(result, "Radiant")

    def test_all_dire(self):
        result = predict_party_victory("DDDD")
        self.assertEqual(result, "Dire")

    def test_single_radiant(self):
        result = predict_party_victory("R")
        self.assertEqual(result, "Radiant")

    def test_single_dire(self):
        result = predict_party_victory("D")
        self.assertEqual(result, "Dire")

    def test_alternating_radiant_wins(self):
        result = predict_party_victory("RDRDRD")
        self.assertEqual(result, "Radiant")

    def test_alternating_dire_wins(self):
        result = predict_party_victory("DRDRDR")
        self.assertEqual(result, "Dire")