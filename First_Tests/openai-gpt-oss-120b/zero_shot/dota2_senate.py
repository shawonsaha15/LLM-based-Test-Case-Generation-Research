def predict_party_victory(senate: str) -> str:
    n = len(senate)
    banned = [False] * n

    ban_r = 0
    ban_d = 0

    active = set()

    while len(active) != 1:
        active = set()

        for i in range(n):
            if banned[i]:
                continue

            party = senate[i]

            if party == 'R':
                if ban_r > 0:
                    ban_r -= 1
                    banned[i] = True
                else:
                    ban_d += 1
                    active.add('R')
            else:
                if ban_d > 0:
                    ban_d -= 1
                    banned[i] = True
                else:
                    ban_r += 1
                    active.add('D')

    winner = active.pop()
    return "Radiant" if winner == 'R' else "Dire"

import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_simple_radiant(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_simple_dire(self):
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_equal_counts_radiant_wins(self):
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")

    def test_equal_counts_dire_wins(self):
        self.assertEqual(predict_party_victory("DRDR"), "Dire")

    def test_long_alternating_radiant(self):
        senate = "RDRDRDRDRD"
        self.assertEqual(predict_party_victory(senate), "Radiant")

    def test_invalid_characters(self):
        result = predict_party_victory("RXD")
        self.assertIn(result, {"Radiant", "Dire"})

    def test_non_string_input_raises(self):
        with self.assertRaises(TypeError):
            predict_party_victory(None)

if __name__ == "__main__":
    unittest.main()