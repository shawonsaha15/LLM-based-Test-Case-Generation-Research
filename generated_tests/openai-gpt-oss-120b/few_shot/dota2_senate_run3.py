import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_simple_alternating(self):
        # Radiant should win when starting with 'R'
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        # Dire should win when starting with 'D'
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_complex_cases(self):
        # Known outcomes from the classic Dota2 Senate problem
        self.assertEqual(predict_party_victory("RDD"), "Radiant")
        self.assertEqual(predict_party_victory("DRR"), "Dire")
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")
        self.assertEqual(predict_party_victory("DDRRR"), "Radiant")
        self.assertEqual(predict_party_victory("RDRDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_long_sequence(self):
        # Long repeating pattern where Radiant should eventually dominate
        senate = "R" * 10 + "D" * 5
        self.assertEqual(predict_party_victory(senate), "Radiant")
        # Long repeating pattern where Dire should eventually dominate
        senate = "D" * 12 + "R" * 3
        self.assertEqual(predict_party_victory(senate), "Dire")