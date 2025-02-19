"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Get the lengths of the haystack and needle
        n, m = len(haystack), len(needle)
        
        # Iterate through the haystack with a window of size equal to the needle
        for i in range(n - m + 1):
            # Check if the substring of haystack matches the needle
            if haystack[i:i + m] == needle:
                return i
        
        # If the needle is not found, return -1
        return -1