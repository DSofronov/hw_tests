from unittest import TestCase
from func_main import solve



class TestCompetitionWinners(TestCase):
    def test_solve(self):
        self.assertEqual(solve([123, 145, 346, 246, 235, 166, 112, 351, 436]),([346, 166, 436], 3))

