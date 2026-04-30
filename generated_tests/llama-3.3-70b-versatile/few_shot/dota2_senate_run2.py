class TestPredictPartyVictory(unittest.TestCase):
    def test_radiant_wins(self):
        result = predict_party_victory("RRRR")
        self.assertEqual(result, "Radiant")

    def test_dire_wins(self):
        result = predict_party_victory("DDDD")
        self.assertEqual(result, "Dire")

    def test_radiant_wins_with_bans(self):
        result = predict_party_victory("RDDDR")
        self.assertEqual(result, "Radiant")

    def test_dire_wins_with_bans(self):
        result = predict_party_victory("DRRDD")
        self.assertEqual(result, "Dire")

    def test_empty_string(self):
        result = predict_party_victory("")
        self.assertEqual(result, "Radiant")

    def test_single_element(self):
        result = predict_party_victory("R")
        self.assertEqual(result, "Radiant")

    def test_alternating_parties(self):
        result = predict_party_victory("RDRDRD")
        self.assertEqual(result, "Radiant")