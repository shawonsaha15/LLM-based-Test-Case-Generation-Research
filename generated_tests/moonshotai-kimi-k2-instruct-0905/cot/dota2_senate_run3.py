import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRDDD"), "Radiant")

    def test_dire_wins(self):
        self.assertEqual(predict_party_victory("DDRRR"), "Dire")

    def test_alternating_radiant_win(self):
        self.assertEqual(predict_party_victory("RDRDRD"), "Radiant")

    def test_alternating_dire_win(self):
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDDD"), "Dire")

    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_two_radiant(self):
        self.assertEqual(predict_party_victory("RR"), "Radiant")

    def test_two_dire(self):
        self.assertEqual(predict_party_victory("DD"), "Dire")

    def test_large_radiant_win(self):
        senate = "R" * 100 + "D" * 50
        self.assertEqual(predict_party_victory(senate), "Radiant")

    def test_large_dire_win(self):
        senate = "D" * 100 + "R" * 50
        self.assertEqual(predict_party_victory(senate), "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_invalid_character(self):
        with self.assertRaises(KeyError):
            predict_party_victory("RXD")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(None)

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(123)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            predict_party_victory(['R', 'D'])

    def test_mixed_case(self):
        with self.assertRaises(KeyError):
            predict_party_victory("RdR")