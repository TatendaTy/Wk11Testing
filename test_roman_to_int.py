import unittest
from roman_to_int import roman_to_int

class RomanToIntTest(unittest.TestCase):
    
    def test_basic_numerals(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("L"), 50)
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("D"), 500)
        self.assertEqual(roman_to_int("M"), 1000)
        
    def test_complex_numerals(self):
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XXIV"), 24)
        self.assertEqual(roman_to_int("LXXXIX"), 89)
        self.assertEqual(roman_to_int("CDXCIV"), 494)
        self.assertEqual(roman_to_int("CMXCIX"), 999)
        
    def test_invalid_input(self):
        self.assertEqual(roman_to_int("XIIII"), "Invalid Roman numeral!")
        self.assertEqual(roman_to_int("MMCDLXXXIIX"), "Invalid Roman numeral!")
        self.assertEqual(roman_to_int("ABC"), "Invalid Roman numeral!")

if __name__ == '__main__':
    unittest.main()

# ---------------------------------------------------------------------------

## REMAINING TESTS

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



