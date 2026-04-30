class TestPredictPartyVictory(unittest.TestCase):
    def test_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_dire_wins(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_radiant_wins_with_bans(self):
        self.assertEqual(predict_party_victory("RDDRR"), "Radiant")

    def test_dire_wins_with_bans(self):
        self.assertEqual(predict_party_victory("DRRDD"), "Dire")

    def test_empty_senate(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_single_member_senate(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_tied_senate(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")