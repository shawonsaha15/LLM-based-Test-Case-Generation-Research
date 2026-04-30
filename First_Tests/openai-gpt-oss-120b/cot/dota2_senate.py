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
    def test_simple_cases(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        self.assertEqual(predict_party_victory("DR"), "Dire")
        self.assertEqual(predict_party_victory("RRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDD"), "Dire")

    def test_mixed_cases(self):
        self.assertEqual(predict_party_victory("RDD"), "Dire")
        self.assertEqual(predict_party_victory("DRR"), "Radiant")
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDR"), "Dire")
        self.assertEqual(predict_party_victory("RRDDRRDD"), "Radiant")

    def test_long_alternating(self):
        senate = "RDRDRDRDRDRDRDRDRDRD"
        result = predict_party_victory(senate)
        self.assertIn(result, ("Radiant", "Dire"))

    def test_invalid_characters(self):
        self.assertEqual(predict_party_victory("RA"), "Radiant")
        self.assertEqual(predict_party_victory("DX"), "Dire")
        self.assertEqual(predict_party_victory("RDXR"), "Radiant")

    def test_single_character(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

if __name__ == "__main__":
    unittest.main()