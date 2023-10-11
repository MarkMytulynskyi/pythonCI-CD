import unittest
from name_function import formatted_name


class NamesTestCase(unittest.TestCase):

   def test_first_last_name(self):
      result = formatted_name("mark", "mytulynskyi", "ivanovych")
      self.assertEqual(result, "Mark Ivanovych Mytulynskyi")


   def test_first_last_middle_name(self):
      result = formatted_name("oleg", "vynnyk", "anatoliyovych")
      self.assertEqual(result, "Oleg Anatoliyovych Vynnyk")
