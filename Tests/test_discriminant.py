from unittest import TestCase
from func_main import discriminant
from func_main import solution


class TestSquareEquation(TestCase):
    def test_discriminant(self):


        self.assertEqual(discriminant(1, 8, 15), 4)
        self.assertEqual(discriminant(1, -13, 12), 121)
        self.assertEqual(discriminant(-4, 28, -49), 0)
        self.assertEqual(discriminant(1, 1, 1), -3)

    def test_solution(self):
        self.assertEqual(solution(1, 8, 15), (-3.0, -5.0))
        self.assertEqual(solution(1, -13, 12), (12.0, 1.0))
        self.assertEqual(solution(-4, 28, -49), (3.5))
        self.assertEqual(solution(1, 1, 1), 'корней нет')


