import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_radiant_wins_simple(self):
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")

    def test_dire_wins_simple(self):
        self.assertEqual(predict_party_victory("DDRR"), "Dire")

    def test_alternating_radiant_wins(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_alternating_dire_wins(self):
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_radiant_majority(self):
        self.assertEqual(predict_party_victory("RRRDDDR"), "Radiant")

    def test_dire_majority(self):
        self.assertEqual(predict_party_victory("DDRRRDD"), "Dire")

    def test_long_sequence_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRRRDDDD"), "Radiant")

    def test_long_sequence_dire_wins(self):
        self.assertEqual(predict_party_victory("DDDDRRRR"), "Dire")

    def test_mixed_sequence_radiant_wins(self):
        self.assertEqual(predict_party_victory("RDRDRDRD"), "Radiant")

    def test_mixed_sequence_dire_wins(self):
        self.assertEqual(predict_party_victory("DRDRDRDR"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDDD"), "Dire")

    def test_two_radiant(self):
        self.assertEqual(predict_party_victory("RR"), "Radiant")

    def test_two_dire(self):
        self.assertEqual(predict_party_victory("DD"), "Dire")