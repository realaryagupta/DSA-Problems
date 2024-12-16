"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array. 

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize the expected number
        expected = 1
        i = 0
        
        while i < len(arr):
            if arr[i] == expected:
                # If the current number is in the array, move to the next number
                i += 1
                expected += 1
            else:
                # If the current number is missing, decrement k
                k -= 1
                if k == 0:
                    return expected
                expected += 1
        
        # If we have checked all numbers in the array and k is still not zero,
        # the k-th missing number is beyond the last number in the array
        return arr[-1] + k