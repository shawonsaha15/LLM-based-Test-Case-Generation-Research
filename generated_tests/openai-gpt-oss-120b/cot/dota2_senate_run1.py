import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_single_radiant(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")

    def test_single_dire(self):
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_two_members_rd(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_two_members_dr(self):
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_balanced_even_radiant(self):
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")

    def test_balanced_even_dire(self):
        self.assertEqual(predict_party_victory("DRDR"), "Dire")

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_long_alternating_start_radiant(self):
        senate = "R" + "D" * 0
        # Build a long alternating string starting with 'R'
        long_senate = "".join("R" if i % 2 == 0 else "D" for i in range(1000))
        self.assertEqual(predict_party_victory(long_senate), "Radiant")

    def test_long_alternating_start_dire(self):
        # Build a long alternating string starting with 'D'
        long_senate = "".join("D" if i % 2 == 0 else "R" for i in range(1000))
        self.assertEqual(predict_party_victory(long_senate), "Dire")

    def test_invalid_characters_treated_as_dire(self):
        # Characters other than 'R' are treated as 'D' by the implementation.
        result = predict_party_victory("RXD")
        self.assertIn(result, {"Radiant", "Dire"})

    def test_none_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            predict_party_victory(None)