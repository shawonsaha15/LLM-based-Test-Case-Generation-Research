import unittest

class TestPredictPartyVictory(unittest.TestCase):

    def test_radiant_wins_single_r(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_dire_wins_single_d(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_radiant_wins_two_rs(self):
        self.assertEqual(predict_party_victory("RR"), "Radiant")

    def test_dire_wins_two_ds(self):
        self.assertEqual(predict_party_victory("DD"), "Dire")

    def test_alternating_rd_radiant_wins(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_alternating_dr_dire_wins(self):
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_radiant_wins_with_banning(self):
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")

    def test_dire_wins_with_banning(self):
        self.assertEqual(predict_party_victory("DRDR"), "Dire")

    def test_radiant_wins_longer_string(self):
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")

    def test_dire_wins_longer_string(self):
        self.assertEqual(predict_party_victory("DDRR"), "Dire")

    def test_radiant_wins_complex_case(self):
        self.assertEqual(predict_party_victory("RRRDDDRRR"), "Radiant")

    def test_dire_wins_complex_case(self):
        self.assertEqual(predict_party_victory("DDRRRRDD"), "Dire")

    def test_radiant_wins_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_dire_wins_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_radiant_wins_mixed_case(self):
        self.assertEqual(predict_party_victory("RDRDRDRD"), "Radiant")

    def test_dire_wins_mixed_case(self):
        self.assertEqual(predict_party_victory("DRDRDRDR"), "Dire")