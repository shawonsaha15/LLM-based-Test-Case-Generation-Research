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
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDDD"), "Dire")
        self.assertEqual(predict_party_victory("RDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDR"), "Dire")

    def test_edge_cases(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")
        self.assertEqual(predict_party_victory("RR"), "Radiant")
        self.assertEqual(predict_party_victory("DD"), "Dire")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            predict_party_victory(123)
        with self.assertRaises(TypeError):
            predict_party_victory(None)
        with self.assertRaises(TypeError):
            predict_party_victory([1, 2, 3])

if __name__ == "__main__":
    unittest.main()