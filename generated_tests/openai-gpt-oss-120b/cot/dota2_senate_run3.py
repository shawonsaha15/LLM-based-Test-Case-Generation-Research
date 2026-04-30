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

    def test_simple_radiant_win(self):
        # R bans D, D gets banned, Radiant wins
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_simple_dire_win(self):
        # D bans R, R gets banned, Dire wins
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_complex_radiant_win(self):
        # Example where Radiant eventually wins
        self.assertEqual(predict_party_victory("RDD"), "Dire")
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")
        self.assertEqual(predict_party_victory("RRDDDR"), "Radiant")

    def test_complex_dire_win(self):
        # Example where Dire eventually wins
        self.assertEqual(predict_party_victory("DRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDRRR"), "Dire")
        self.assertEqual(predict_party_victory("DDRRDR"), "Dire")

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            predict_party_victory(None)

    def test_invalid_input_other_char(self):
        # Characters other than 'R' or 'D' are treated as 'D' by the implementation,
        # but this is considered invalid usage; we expect it to still return a result
        # without raising an exception.
        result = predict_party_victory("RXD")
        self.assertIn(result, ("Radiant", "Dire"))

    def test_large_input(self):
        # Large alternating sequence; Radiant should win because it starts first.
        large_input = ("RD" * 5000)  # 10,000 characters
        self.assertEqual(predict_party_victory(large_input), "Radiant")

    def test_unbalanced_large_input(self):
        # Large input heavily favoring Dire
        large_input = "D" * 8000 + "R" * 2000
        self.assertEqual(predict_party_victory(large_input), "Dire")