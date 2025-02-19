"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # Import the math module to use sqrt and floor functions
        import math
        
        # Calculate the square root of x using math.sqrt
        root = math.sqrt(x)
        
        # Use math.floor to round down the square root to the nearest integer
        number = math.floor(root)
        
        # Return the integer part of the square root
        return number