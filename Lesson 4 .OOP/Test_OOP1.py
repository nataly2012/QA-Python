import unittest
from OOP1 import  ITEmpl
class EmplTest(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmpl("Nata", "Pin")

    def test_name(self):
        self.assertEqual (self.emp.name, "Nata")
        self.assertEqual (self.emp.surname, "Pin")