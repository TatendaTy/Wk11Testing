import unittest
from roman_to_int import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int(self):
        # Test valid input
        self.assertEqual(roman_to_int.roman_to_int('I'), 1)
        self.assertEqual(roman_to_int.roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int.roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int.roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int.roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int.roman_to_int('MCMXCIV'), 1994)

        # Test invalid input
        with self.assertRaises(KeyError):
            roman_to_int('A')
        with self.assertRaises(KeyError):
            roman_to_int('IIII')
        with self.assertRaises(KeyError):
            roman_to_int('MMMM')
        with self.assertRaises(KeyError):
            roman_to_int('IC')
    
if __name__ == '__main__':
    unittest.main()

# def test_roman_to_int():
#     # Test valid input
#     assert roman_to_int('I') == 1
#     assert roman_to_int('IV') == 4
#     assert roman_to_int('IX') == 9
#     assert roman_to_int('XL') == 40
#     assert roman_to_int('CD') == 400
#     assert roman_to_int('MCMXCIV') == 1994

#     # Test invalid input
#     with pytest.raises(KeyError):
#         roman_to_int('A')
#     with pytest.raises(KeyError):
#         roman_to_int('IIII')
#     with pytest.raises(KeyError):
#         roman_to_int('MMMM')
#     with pytest.raises(KeyError):
#         roman_to_int('IC')
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



