import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_simple_cases(self):
        # Basic alternating cases
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        self.assertEqual(predict_party_victory("DR"), "Dire")
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDR"), "Dire")

    def test_all_same_party(self):
        # All members belong to the same party
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_mixed_longer_cases(self):
        # Longer mixed strings where the outcome is known
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")
        self.assertEqual(predict_party_victory("DDRR"), "Dire")
        self.assertEqual(predict_party_victory("RDRRDRDD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDRDRRRDD"), "Dire")

    def test_invalid_input_none(self):
        # Passing None should raise a TypeError because len(None) is invalid
        with self.assertRaises(TypeError):
            predict_party_victory(None)

    def test_invalid_input_non_string(self):
        # Non‑string iterable (e.g., integer) should also raise a TypeError
        with self.assertRaises(TypeError):
            predict_party_victory(12345)

    def test_large_input_performance(self):
        # Large alternating pattern; should complete quickly and give correct result
        large_input = "RDRD" * 250  # length 1000
        # Expected winner for a perfectly alternating long sequence is Radiant
        self.assertEqual(predict_party_victory(large_input), "Radiant")