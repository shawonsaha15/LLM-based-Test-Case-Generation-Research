import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins_simple(self):
        self.assertEqual(predict_party_victory("RRDDD"), "Radiant")

    def test_dire_wins_simple(self):
        self.assertEqual(predict_party_victory("DDRRR"), "Dire")

    def test_radiant_wins_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_dire_wins_all_dire(self):
        self.assertEqual(predict_party_victory("DDDDD"), "Dire")

    def test_alternating_radiant_wins(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_alternating_dire_wins(self):
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_complex_case_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRRDDD"), "Radiant")

    def test_complex_case_dire_wins(self):
        self.assertEqual(predict_party_victory("DDRRRR"), "Dire")

    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_radiant_bans_dire_then_wins(self):
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")

    def test_dire_bans_radiant_then_wins(self):
        self.assertEqual(predict_party_victory("DDRR"), "Dire")

    def test_longer_mixed_sequence(self):
        self.assertEqual(predict_party_victory("RDRDRDRD"), "Radiant")

    def test_longer_dire_majority(self):
        self.assertEqual(predict_party_victory("DDRDRDRD"), "Dire")

    def test_radiant_majority_with_dire_first(self):
        self.assertEqual(predict_party_victory("DRRRDDD"), "Radiant")

    def test_dire_majority_with_radiant_first(self):
        self.assertEqual(predict_party_victory("RDDDRR"), "Dire")