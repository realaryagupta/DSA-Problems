"""
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Initialize the total score to 0
        total_score = 0
        
        # Iterate through the string, except the last character
        for i in range(len(s) - 1):
            # Get the ASCII value of the current character
            ascii_code_current = ord(s[i])
            # Get the ASCII value of the next character
            ascii_code_next = ord(s[i + 1])
            # Add the absolute difference between the two ASCII values to the total score
            total_score += abs(ascii_code_current - ascii_code_next)
        
        # Return the total score
        return total_score