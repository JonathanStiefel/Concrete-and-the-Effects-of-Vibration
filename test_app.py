import unittest
from app import App

# RUN via Shell:
# python -m unittest


class TestStringMethods(unittest.TestCase):

  def setUp(self):
    self.app = App(False)
    self.app.setup()

  def test__init__(self):
    self.assertTrue(isinstance(self.app, App))


#python -m unittest
# that tests the code
