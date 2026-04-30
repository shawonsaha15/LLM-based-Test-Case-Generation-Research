class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_dire_wins(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_radiant_wins_with_bans(self):
        self.assertEqual(predict_party_victory("RRDRDR"), "Radiant")

    def test_dire_wins_with_bans(self):
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_single_character(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_tie(self):
        with self.assertRaises(ValueError):
            predict_party_victory("RD")