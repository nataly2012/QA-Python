import unittest
from it_emp import ITEmployee

class EmplTests(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee('Elena Pian')
        self.emp.add_skill('Git')

    def test_names(self):
        self.assertEquals(self.emp.full_name, 'Elena Pian')


    def test_no_position(self):
        self.assertIsNone(self.emp.position)

    def test_skill(self):
        self.assertEquals(self.emp.skills[0], 'Git')

    def test_position(self):
        self.assertEquals(self.emp.pos(), 'Junior')

if __name__ == "__main__":
    unittest.main()