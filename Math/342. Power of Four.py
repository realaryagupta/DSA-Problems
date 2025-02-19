"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Initialize an empty list to store powers of 4
        pwr_of_4 = []

        # Loop through the first 32 powers of 4 (since 4^16 is the largest power of 4 within 32-bit integer range)
        for i in range(32):
            # Calculate 4 raised to the power of i
            num = 4 ** i
            # Append the result to the list
            pwr_of_4.append(num)
        
        # Check if n is in the list of powers of 4
        if n in pwr_of_4:
            return True
        else:
            return False