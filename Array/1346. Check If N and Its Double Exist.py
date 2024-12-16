"""
Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Initialize an empty set to store elements
        tmp = set()

        # Iterate through each element in the array
        for i in arr:
            # Check if the double of the current element or half of the current even element exists in the set
            if 2 * i in tmp or (i % 2 == 0 and i / 2 in tmp):
                return True
            # Add the current element to the set
            tmp.add(i)
        
        # If no such pair is found, return False
        return False