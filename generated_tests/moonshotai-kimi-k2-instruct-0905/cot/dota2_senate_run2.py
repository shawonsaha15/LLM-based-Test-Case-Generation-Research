import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins_simple(self):
        self.assertEqual(predict_party_victory("RRDDD"), "Radiant")

    def test_dire_wins_simple(self):
        self.assertEqual(predict_party_victory("DDRRR"), "Dire")

    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_alternating_parties_radiant_first(self):
        self.assertEqual(predict_party_victory("RDD"), "Radiant")

    def test_alternating_parties_dire_first(self):
        self.assertEqual(predict_party_victory("DRR"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_large_input_radiant_wins(self):
        senate = "R" * 1000 + "D" * 999
        self.assertEqual(predict_party_victory(senate), "Radiant")

    def test_large_input_dire_wins(self):
        senate = "D" * 1000 + "R" * 999
        self.assertEqual(predict_party_victory(senate), "Dire")

    def test_invalid_characters(self):
        with self.assertRaises(KeyError):
            predict_party_victory("RXD")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(None)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(123)

    def test_mixed_case_input(self):
        with self.assertRaises(KeyError):
            predict_party_victory("RrDd")