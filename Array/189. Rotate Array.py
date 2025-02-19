"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.    
        """
        n = len(nums)

        k = k % n # Handle cases where k is larger than the length of nums

        # Use slicing to rotate the list in-place
        nums[:] = nums[-k:] + nums[:-k]

        # If i had been using the below then it will 

        # nums = nums[:k] + nums[k:]

        # the above code does not actually modify the original list nums in-place. 
        # Instead, it creates a new list by concatenating the two slices nums[:k] and nums[k:], 
        # and then assigns this new list to the variable nums. This reassignment does not affect the original list that was passed to the function, 
        # so the modification is not reflected outside the function.