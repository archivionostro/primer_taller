import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'funciones'))

from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
