import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'funciones'))

from par import es_par

class TestPar(unittest.TestCase):
    def test_par_con_4(self):
        self.assertTrue(es_par(4))

    def test_par_con_5(self):
        self.assertFalse(es_par(5))

if __name__ == '__main__':
    unittest.main()
