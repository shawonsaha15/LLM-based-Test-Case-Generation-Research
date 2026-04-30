import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_simple_alternating(self):
        # Radiant bans Dire, then Dire bans Radiant, Radiant wins
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        # Dire bans Radiant, then Radiant bans Dire, Dire wins
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_balanced_sequence(self):
        # Classic example where Radiant eventually wins
        self.assertEqual(predict_party_victory("RDD"), "Radiant")
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDR"), "Dire")

    def test_complex_cases(self):
        # Longer mixed sequences
        self.assertEqual(predict_party_victory("RRDDRRDD"), "Radiant")
        self.assertEqual(predict_party_victory("RDRDRDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDRDRDR"), "Dire")
        self.assertEqual(predict_party_victory("RRRDRDDDRRDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DDDRRDRRDRDDRR"), "Dire")