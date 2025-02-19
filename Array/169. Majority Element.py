"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
 
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the count of each number
        num_count = {}

        # Count the occurrences of each number in the list
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Iterate through the dictionary to find the majority element
        for num in num_count:
            if num_count[num] > len(nums) / 2:
                return num