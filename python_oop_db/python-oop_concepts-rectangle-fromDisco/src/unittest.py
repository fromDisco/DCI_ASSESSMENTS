import unittest

class TestClassMethods(unittest.TestCase):
      
    def test_area(self):        
        self.assertEqual(self.get_area(), 221)


if __name__ == "__main__":
    unittest.main()