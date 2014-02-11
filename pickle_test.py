import unittest
from pickler import favorite_color, fave_color
class PickleTest (unittest.TestCase):
  def pickler_same_unpickler_test(self):
    self.assertEqual (favorite_color,fave_color)