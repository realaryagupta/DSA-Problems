"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space. 

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize the left and right pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search to find the single non-duplicate element
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # Ensure the mid index is even
            if mid % 2 == 1:
                mid -= 1  

            # If the middle element is equal to the next element, the single element is on the right side
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            # Otherwise, the single element is on the left side
            else:
                right = mid

        # Return the single non-duplicate element
        return nums[left]