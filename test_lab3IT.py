import unittest
from name_function import formatted_name


def test_first_last_name():
   result = formatted_name("mark", "mytulynskyi", "ivanovych")
   pib = "Mark Ivanovych Mytulynskyi"
   assert pib in result
#132132

def test_first_last_middle_name():
   result = formatted_name("oleg", "vynnyk", "anatoliyovych")
   pib = "Oleg Anatoliyovych Vynnyk"
   assert pib in result
