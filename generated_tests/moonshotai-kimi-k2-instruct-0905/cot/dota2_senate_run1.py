import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins_simple(self):
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")

    def test_dire_wins_simple(self):
        self.assertEqual(predict_party_victory("DDRR"), "Dire")

    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_alternating_radiant_wins(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_alternating_dire_wins(self):
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_large_radiant_majority(self):
        self.assertEqual(predict_party_victory("RRRRRDDDD"), "Radiant")

    def test_large_dire_majority(self):
        self.assertEqual(predict_party_victory("DDDDDRRRR"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_invalid_characters(self):
        with self.assertRaises(KeyError):
            predict_party_victory("RXD")

    def test_mixed_case(self):
        with self.assertRaises(KeyError):
            predict_party_victory("RdDr")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(None)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(123)

    def test_long_string_radiant_wins(self):
        senate = "R" * 100 + "D" * 99
        self.assertEqual(predict_party_victory(senate), "Radiant")

    def test_long_string_dire_wins(self):
        senate = "D" * 100 + "R" * 99
        self.assertEqual(predict_party_victory(senate), "Dire")

    def test_complex_sequence_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRDDDRRR"), "Radiant")

    def test_complex_sequence_dire_wins(self):
        self.assertEqual(predict_party_victory("DDRRRDDD"), "Dire")