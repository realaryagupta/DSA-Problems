"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

class Solution:
    def binarySearch(self, nums, low, high, target):
        # Base case: if low index exceeds high index, target is not found
        if low > high:
            return -1
            
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the middle element is the target, return its index
        if nums[mid] == target:
            return mid
        # If the middle element is less than the target, search the right half
        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, high, target)
        # Otherwise, search the left half
        return self.binarySearch(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        # Call the binary search function with initial low and high indices
        return self.binarySearch(nums, 0, len(nums) - 1, target)