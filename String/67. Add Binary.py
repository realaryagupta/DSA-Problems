"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert to decimal
        a = int(a,2)
        b = int(b,2)

        # convert sum to binary
        sum = bin(a + b)

        # the output will contain '0b' prefix so removing them 
        sum = sum[2:]
        
        return sum
