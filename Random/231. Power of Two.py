"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x. 

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Initialize an empty list to store powers of 2
        arr = []

        # Loop through the first 32 powers of 2 (since 2^31 is the largest power of 2 within 32-bit integer range)
        for i in range(0, 32):
            # Calculate 2 raised to the power of i
            a = 2 ** i
            # Append the result to the list
            arr.append(a)

        # Loop through the list of powers of 2
        for i in arr:
            # Check if n matches any of the powers of 2
            if n == i:
                return True

        # If no match is found, return False
        return False