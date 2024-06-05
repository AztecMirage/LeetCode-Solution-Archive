# Example Walkthrough
# Converting "MCMXCIV" to an integer:

# Initialize total to 0 and prev_value to 0.
# Iterate through the string in reverse ("V", "I", "C", "X", "M", "C", "M"):

# 'V' (5): Add 5 to total → total = 5
# 'I' (1): Since 1 < 5, subtract 1 from total → total = 4
# 'C' (100): Add 100 to total → total = 104
# 'X' (10): Since 10 < 100, subtract 10 from total → total = 94
# 'M' (1000): Add 1000 to total → total = 1094
# 'C' (100): Since 100 < 1000, subtract 100 from total → total = 994
# 'M' (1000): Add 1000 to total → total = 1994

# Finally, total is 1994, which is the integer value of "MCMXCIV".

# Code
def romanToInt(s: str) -> int:
    # Mapping
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialization
    total = 0
    prev_value = 0
    
    # Iteration
    for char in reversed(s):
        current_value = roman_to_int[char]
    # Subraction or Addition
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    # Value
    return total
