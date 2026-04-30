import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_single_member(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_two_members(self):
        cases = [
            ("RD", "Radiant"),
            ("DR", "Dire")
        ]
        for senate, expected in cases:
            with self.subTest(senate=senate):
                self.assertEqual(predict_party_victory(senate), expected)

    def test_various_patterns(self):
        cases = [
            ("RRDD", "Radiant"),
            ("DDRR", "Dire"),
            ("RDRD", "Radiant"),
            ("DRDR", "Dire"),
            ("RRRDDD", "Radiant"),
            ("DDDRRR", "Dire")
        ]
        for senate, expected in cases:
            with self.subTest(senate=senate):
                self.assertEqual(predict_party_victory(senate), expected)

    def test_equal_majority(self):
        senate = "R" * 5 + "D" * 5
        self.assertEqual(predict_party_victory(senate), "Radiant")

    def test_long_alternating(self):
        senate = "RD" * 50
        self.assertEqual(predict_party_victory(senate), "Radiant")
        senate = "DR" * 50
        self.assertEqual(predict_party_victory(senate), "Dire")