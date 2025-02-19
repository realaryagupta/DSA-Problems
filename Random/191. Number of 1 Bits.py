"""
Given a positive integer n, write a function that returns the number of  set bits in its binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer n to its binary representation using bin()
        n = bin(n)
        
        # Remove the '0b' prefix from the binary string
        n = n[2:]
        
        # Convert the binary string to a regular string
        n = str(n)
        
        # Initialize a counter to count the number of '1's
        counter = 0
        
        # Iterate through each character in the binary string
        for i in n:
            # If the character is '1', increment the counter
            if i == "1":
                counter = counter + 1
        
        # Return the total count of '1's
        return counter