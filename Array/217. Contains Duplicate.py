"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Calculate the length of the input list
        length_arr = len(nums)

        # Convert the list to a set to eliminate duplicates
        hash_set = set(nums)

        # If the length of the set is equal to the length of the list, there are no duplicates
        if length_arr == len(hash_set):
            return False
        else:
            # Otherwise, there are duplicates
            return True