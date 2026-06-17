import unittest 
import fizzbuzz 

class TestFizzBuzz(unittest.TestCase):
    def test_returns_number_as_string(self):
        self.assertEqual(fizzbuzz.fizzbuzz_logic(1), "1")

if __name__== '__main__':
    unittest.main()