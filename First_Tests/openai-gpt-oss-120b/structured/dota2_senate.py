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
    def test_normal_cases(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        self.assertEqual(predict_party_victory("DR"), "Dire")
        self.assertEqual(predict_party_victory("RDD"), "Dire")
        self.assertEqual(predict_party_victory("RRDD"), "Radiant")
        self.assertEqual(predict_party_victory("DRRDRDRDRDDRDRDR"), "Radiant")

    def test_edge_cases(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")
        self.assertEqual(predict_party_victory("RRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDD"), "Dire")
        self.assertEqual(predict_party_victory("RDRDRDRDRD"), "Radiant")

    def test_invalid_inputs(self):
        self.assertEqual(predict_party_victory("rD"), "Dire")
        self.assertEqual(predict_party_victory("R1D"), "Dire")
        self.assertEqual(predict_party_victory("XYZ"), "Dire")
        self.assertEqual(predict_party_victory(""), None)

if __name__ == "__main__":
    unittest.main()