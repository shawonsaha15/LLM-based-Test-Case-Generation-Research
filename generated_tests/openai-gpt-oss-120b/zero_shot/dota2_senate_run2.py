import unittest

class TestPredictPartyVictory(unittest.TestCase):
    def test_simple_radiant_win(self):
        # One Radiant member bans the Dire member
        self.assertEqual(predict_party_victory("RD"), "Radiant")

    def test_simple_dire_win(self):
        # One Dire member bans the Radiant member
        self.assertEqual(predict_party_victory("DR"), "Dire")

    def test_all_radiant(self):
        # All members are Radiant, Radiant should win immediately
        self.assertEqual(predict_party_victory("RRRRR"), "Radiant")

    def test_all_dire(self):
        # All members are Dire, Dire should win immediately
        self.assertEqual(predict_party_victory("DDDD"), "Dire")

    def test_alternating_start_radiant(self):
        # Alternating members, Radiant starts and should eventually win
        self.assertEqual(predict_party_victory("RDRDRD"), "Radiant")

    def test_alternating_start_dire(self):
        # Alternating members, Dire starts and should eventually win
        self.assertEqual(predict_party_victory("DRDRDR"), "Dire")

    def test_complex_case_1(self):
        # Mixed sequence where Radiant eventually dominates
        self.assertEqual(predict_party_victory("RRDDRRD"), "Radiant")

    def test_complex_case_2(self):
        # Mixed sequence where Dire eventually dominates
        self.assertEqual(predict_party_victory("DDRRDRRDRD"), "Dire")

    def test_long_sequence(self):
        # Longer sequence to test performance and correctness
        senate = "RDRRDRDRRRDDDRDRRDRDRRRDDDRDRRDRDRRRDDDRDRRDRDRRRDDDRDRRDRDRRRDDDR"
        # Manually verified expected winner is Radiant
        self.assertEqual(predict_party_victory(senate), "Radiant")