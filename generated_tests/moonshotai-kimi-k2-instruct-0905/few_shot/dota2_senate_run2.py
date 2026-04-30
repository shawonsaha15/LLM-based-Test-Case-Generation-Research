class TestPredictPartyVictory(unittest.TestCase):
    def test_radiant_wins(self):
        result = predict_party_victory("RRDD")
        self.assertEqual(result, "Radiant")

    def test_dire_wins(self):
        result = predict_party_victory("DDRR")
        self.assertEqual(result, "Dire")

    def test_single_radiant(self):
        result = predict_party_victory("R")
        self.assertEqual(result, "Radiant")

    def test_single_dire(self):
        result = predict_party_victory("D")
        self.assertEqual(result, "Dire")

    def test_alternating_radiant_wins(self):
        result = predict_party_victory("RD")
        self.assertEqual(result, "Radiant")

    def test_alternating_dire_wins(self):
        result = predict_party_victory("DR")
        self.assertEqual(result, "Dire")

    def test_radiant_majority(self):
        result = predict_party_victory("RRRDDD")
        self.assertEqual(result, "Radiant")

    def test_dire_majority(self):
        result = predict_party_victory("DDDDRR")
        self.assertEqual(result, "Dire")

    def test_long_sequence_radiant_wins(self):
        result = predict_party_victory("RRDDDD")
        self.assertEqual(result, "Dire")

    def test_long_sequence_dire_wins(self):
        result = predict_party_victory("DDRRRR")
        self.assertEqual(result, "Radiant")