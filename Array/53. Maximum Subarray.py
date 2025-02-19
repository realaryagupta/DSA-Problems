"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the result to the first element of the array
        res = nums[0]
        
        # Initialize a variable to keep track of the current subarray sum
        total = 0

        # Iterate through each number in the array
        for n in nums:
            # If the current subarray sum is negative, reset it to 0
            # This is because a negative sum would not contribute to a larger sum
            if total < 0:
                total = 0

            # Add the current number to the subarray sum
            total += n
            
            # Update the result with the maximum of the current result and the subarray sum
            res = max(res, total)
        
        # Return the maximum subarray sum found
        return res