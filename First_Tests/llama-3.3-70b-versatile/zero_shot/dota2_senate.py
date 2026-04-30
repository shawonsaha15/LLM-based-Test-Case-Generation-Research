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
    def test_radiant_wins(self):
        self.assertEqual(predict_party_victory("RRRR"), "Radiant")

    def test_dire_wins(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_radiant_wins_with_bans(self):
        self.assertEqual(predict_party_victory("RDDRR"), "Radiant")

    def test_dire_wins_with_bans(self):
        self.assertEqual(predict_party_victory("DRRDD"), "Dire")

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_single_character(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            predict_party_victory("RXD")

    def test_long_string(self):
        self.assertEqual(predict_party_victory("RRRRRRRRRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDDDDDDDDD"), "Dire")

if __name__ == "__main__":
    unittest.main()