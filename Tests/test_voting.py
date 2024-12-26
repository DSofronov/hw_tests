from unittest import TestCase
from func_main import vote



class TestVoting(TestCase):
    def test_vote(self):
        self.assertEqual(vote([1, 1, 1, 2, 3]),1)
        self.assertEqual(vote([1, 2, 3, 2 ,2]), 2)