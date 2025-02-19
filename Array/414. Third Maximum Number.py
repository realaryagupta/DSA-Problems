"""
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remove duplicates by converting the list to a set, then back to a list
        unique_nums = list(set(nums))
        # Sort the unique numbers in descending order
        unique_nums.sort(reverse=True)

        # If there are at least three unique numbers, return the third maximum
        if len(unique_nums) >= 3:
            return unique_nums[2]
        else:
            # Otherwise, return the maximum number
            return unique_nums[0]