# Process
# We have to determine whether a given non-negative integer c can be expressed as the sum of the squares of two integers.
# In other words, you need to check if there exist two non-negative integers a and b such that:
# To solve this problem, we can use the two-pointer technique.
# The idea is to use one pointer starting from 0 and the other starting from the square root of c,
# and adjust the pointers based on the current sum of their squares.

# Solution
import math
def judgeSquareSum(c: int) -> bool:
    a = 0
    b = int(math.sqrt(c))
    
    while a <= b:
        current_sum = a * a + b * b
        if current_sum == c:
            return True
        elif current_sum < c:
            a += 1
        else:
            b -= 1
    
    return False
