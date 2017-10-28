import unittest
from UnitTest import dis

class DistanceTests(unittest.TestCase):
    def test_zero(self):
      res = distance(0,0,0,0)
      self.assertEqual (res,0)

    def test_two(self):
        res = distance(2,2,2,2)
        self.assertEqual (res,3)
