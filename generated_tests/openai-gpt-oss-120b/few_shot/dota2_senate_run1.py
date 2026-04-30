import unittest
import random
from collections import deque

class TestPredictPartyVictory(unittest.TestCase):
    def simulate_with_queues(self, senate: str) -> str:
        """Reference implementation using queues (the classic solution)."""
        radiant = deque(i for i, c in enumerate(senate) if c == 'R')
        dire = deque(i for i, c in enumerate(senate) if c == 'D')
        n = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"

    def test_all_radiant(self):
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_all_dire(self):
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_single_member(self):
        self.assertEqual(predict_party_victory("R"), "Radiant")
        self.assertEqual(predict_party_victory("D"), "Dire")

    def test_simple_alternating(self):
        self.assertEqual(predict_party_victory("RD"), "Radiant")
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_known_example(self):
        # LeetCode example: "RDD" -> Radiant
        self.assertEqual(predict_party_victory("RDD"), "Radiant")
        # Another example: "DRRDRDRDRDDRDRDR" (random but deterministic)
        senate = "DRRDRDRDRDDRDRDR"
        expected = self.simulate_with_queues(senate)
        self.assertEqual(predict_party_victory(senate), expected)

    def test_random_cases(self):
        for _ in range(50):
            length = random.randint(1, 12)
            senate = ''.join(random.choice('RD') for _ in range(length))
            expected = self.simulate_with_queues(senate)
            result = predict_party_victory(senate)
            self.assertEqual(result, expected, f"Failed for senate={senate}")