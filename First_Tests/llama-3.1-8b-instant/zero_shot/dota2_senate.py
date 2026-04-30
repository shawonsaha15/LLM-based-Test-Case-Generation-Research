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
    def test_normal_case(self):
        self.assertEqual(predict_party_victory("RDDRR"), "Radiant")
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_edge_case_equal_bans(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")
        self.assertEqual(predict_party_victory("DDDDD"), "Dire")

    def test_edge_case_no_bans(self):
        self.assertEqual(predict_party_victory("RDRDRD"), "Radiant")
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_edge_case_all_banned(self):
        self.assertEqual(predict_party_victory("RDRDRD" + "R" * 10), "Radiant")
        self.assertEqual(predict_party_victoy("DRDRDR" + "D" * 10), "Dire")

    def test_invalid_input_empty_string(self):
        with self.assertRaises(IndexError):
            predict_party_victory("")

    def test_invalid_input_single_character(self):
        with self.assertRaises(IndexError):
            predict_party_victory("R")

    def test_invalid_input_no_repeats(self):
        with self.assertRaises(IndexError):
            predict_party_victory("RD")

    def test_invalid_input_repeats_only_one_party(self):
        with self.assertRaises(IndexError):
            predict_party_victory("RRRRR")

    def test_invalid_input_repeats_only_other_party(self):
        with self.assertRaises(IndexError):
            predict_party_victory("DDDDD")

if __name__ == "__main__":
    unittest.main()