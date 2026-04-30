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
    def test_basic(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRR"), "Radiant")
        self.assertEqual(predict_party_victory("RRRD"), "Radiant")

    def test_dire_wins(self):
        self.assertEqual(predict_party_victory("DDD"), "Dire")
        self.assertEqual(predict_party_victory("DDDR"), "Dire")

    def test_long_sequence(self):
        self.assertEqual(predict_party_victory("RRRRRRRRRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDDDDDDDDD"), "Dire")

if __name__ == "__main__":
    unittest.main()