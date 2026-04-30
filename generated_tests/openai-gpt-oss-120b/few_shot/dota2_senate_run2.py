import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_simple_pairs(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_alternating_sequences(self):
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDR"), "Dire")
        self.assertEqual(predict_party_victory("RDRDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_unequal_counts(self):
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")
        self.assertEqual(predict_party_victory("DDRR"), "Dire")
        self.assertEqual(predict_party_victory("RRRDDD"), "Radiant")
        self.assertEqual(predict_party_victory("DDDRRR"), "Dire")

    def test_complex_patterns(self):
        self.assertEqual(predict_party_victory("RDRRDDR"), "Radiant")
        self.assertEqual(predict_party_victory("DRDDRRR"), "Dire")
        self.assertEqual(predict_party_victory("RRDDRRDDRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDRRDDRRDD"), "Dire")