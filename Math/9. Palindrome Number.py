"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, it cannot be a palindrome
        if x < 0:
            return False

        # Convert the integer to a string for easy comparison
        string = str(x)

        # Initialize two pointers: one at the start and one at the end of the string
        i = 0
        j = len(string) - 1

        # Loop through the string
        for i in range(len(string)-1):  # Iterate from the start to the second-last character
            # Compare characters at the two pointers
            if string[i] == string[j]:
                # Move the pointers towards the center
                i = i + 1
                j = j - 1
            else:
                # If characters don't match, it's not a palindrome
                return False

        # If all characters matched, it's a palindrome
        return True