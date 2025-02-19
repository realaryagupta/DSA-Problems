"""
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Handle negative numbers
        if num < 0:
            return False
        
        # Handle edge cases: 0 and 1
        if num in (0, 1):
            return True

        # Iterate through numbers from 1 to num
        for i in range(1, num + 1):
            # Check if the square of i equals num
            if i * i == num:
                return True
            # If the square of i exceeds num, break the loop
            if i * i > num:
                break
        
        # If no perfect square is found, return False
        return False