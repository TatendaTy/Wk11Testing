import unittest
from roman_to_int import roman_to_int

# this code tests 
# Single Letters:I, V, X, L, C, D, M.
# Many Letters: XI
# Subtractive notation (SN):IV
# With and without SN:XIV
# Repetition:II
# First number:I
# inValid Letter:Z
# Invalid and valid Letter: XIZ
# Not Valid:VV
# Null:
class RomanToIntTest(unittest.TestCase):
    def test_single_letters(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        
    def test_many_letters(self):
        self.assertEqual(roman_to_int('XI'), 11)
        self.assertEqual(roman_to_int('CCC'), 300)
        self.assertEqual(roman_to_int('MDCLXVI'), 1666)
        
    def test_subtractive_notation(self):
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('CM'), 900)
        
    def test_with_and_without_subtractive_notation(self):
        self.assertEqual(roman_to_int('XIV'), 14)
        self.assertEqual(roman_to_int('XXXIX'), 39)
        self.assertEqual(roman_to_int('CXLIV'), 144)
        
    def test_repetition(self):
        self.assertEqual(roman_to_int('II'), 2)
        self.assertEqual(roman_to_int('XXX'), 30)
        self.assertEqual(roman_to_int('CCC'), 300)
        
    def test_first_number(self):
        self.assertEqual(roman_to_int('I'), 1)
        
    def test_invalid_letter(self):
        with self.assertRaises(ValueError):
            roman_to_int('Z')
            
    def test_invalid_and_valid_letter(self):
        with self.assertRaises(ValueError):
            roman_to_int('XIZ')
        
    def test_not_valid(self):
        with self.assertRaises(ValueError):
            roman_to_int('VV')
        
    def test_null(self):
        self.assertEqual(roman_to_int(''), 0)

if __name__ == '__main__':
    unittest.main()

# ---------------------------------------------------------------------------

