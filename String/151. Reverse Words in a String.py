"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove leading and trailing whitespace and split the string into words
        string = s.strip().split()

        # Initialize two pointers for reversing the list of words
        left, right = 0, len(string) - 1
        
        # Reverse the list of words using the two pointers
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        # Join the reversed list of words into a single string with spaces
        return " ".join(string)