class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_dire_wins(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_radiant_wins_after_bans(self):
        self.assertEqual(predict_party_victory("RDDRR"), "Radiant")

    def test_dire_wins_after_bans(self):
        self.assertEqual(predict_party_victory("DRRDD"), "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_single_character_string(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_long_string(self):
        self.assertEqual(predict_party_victory("RRRRRRRRRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDDDDDDDDD"), "Dire")