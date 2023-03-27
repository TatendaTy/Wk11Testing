# Define a function to convert Roman numerals to integers
def roman_to_int(s):
    # Create a dictionary of Roman numeral symbols and their integer values
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the result variable
    result = 0
    
    # Loop through the input string
    for i in range(len(s)):
        # Get the integer value of the current symbol
        value = roman_dict[s[i]]
        
        # If the current symbol is the last one or has a greater value than the next symbol,
        # add its value to the result
        if i == len(s) - 1 or roman_dict[s[i+1]] <= value:
            result += value
        # Otherwise, subtract its value from the result
        else:
            result -= value
    
    # Return the result
    return result

# Ask the user for input
roman_numeral = input("Enter a Roman numeral: ").upper()

# Check if the input is a valid Roman numeral
valid = all(c in "IVXLCDM" for c in roman_numeral)
if not valid:
    print("Invalid Roman numeral!")
else:
    # Convert the Roman numeral to an integer
    integer = roman_to_int(roman_numeral)
    
    # Print the result
    print(f"The integer value of {roman_numeral} is {integer}.")
