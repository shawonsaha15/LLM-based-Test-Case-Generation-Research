class TestPredictPartyVictory(unittest.TestCase):
    def test_radiant_wins(self):
        result = predict_party_victory("RRRR")
        self.assertEqual(result, "Radiant")

    def test_dire_wins(self):
        result = predict_party_victory("DDDD")
        self.assertEqual(result, "Dire")

    def test_radiant_wins_with_bans(self):
        result = predict_party_victory("RDRDRDRD")
        self.assertEqual(result, "Radiant")

    def test_dire_wins_with_bans(self):
        result = predict_party_victory("DRDRDRDRD")
        self.assertEqual(result, "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_single_member(self):
        result = predict_party_victory("R")
        self.assertEqual(result, "Radiant")

    def test_single_member_dire(self):
        result = predict_party_victory("D")
        self.assertEqual(result, "Dire")