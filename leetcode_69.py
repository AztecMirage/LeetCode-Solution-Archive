# Function Definition:
# Define a function called square_root that takes an integer n as input.

# Check for Special Cases:
# If the input number n is 0 or 1, it returns n immediately, as the square root of 0 or 1 is the number itself.

# Initialization:
# Initialize two variables, x and y, with initial guesses for the square root. x is set to the input number n, and y is set to 1.

# Iterative Refinement:
# Enter a loop that continues until the absolute difference between x and y is less than or equal to 1 (The Babylonian method)

# In each iteration: (Formula)
# x is updated to the average of x and y.
# y is updated to the integer division of n by the updated value of x.

# Return the Result:
# Once the loop terminates, we return the minimum of x and y as the rounded square root.

# For the input number 8:
# Initially, x = 8 and y = 1.
# After iterations, x converges to 3 and y converges to 2.
# We return the minimum of 3 and 2, which is 2.

def square_root(n):
    if n == 0 or n == 1:
        return n
    
    x = n
    y = 1

    # The Babylonian method, also known as Heron's method, is an ancient algorithm used to approximate the square root of a number.
    # It's an iterative method that repeatedly refines the estimate of the square root until it reaches a satisfactory level of accuracy.
    while abs(x - y) > 1:
        x = (x + y) // 2
        y = n // x

    return min(x, y)

