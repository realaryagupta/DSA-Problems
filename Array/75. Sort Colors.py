"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Initialize pointers for the three partitions
        low = 0  # Pointer for 0s
        mid = 0  # Pointer for 1s
        high = len(nums) - 1  # Pointer for 2s

        # Iterate through the array until the mid pointer crosses the high pointer
        while mid <= high:
            # If the current element is 0, swap it with the element at the low pointer
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1  # Move the low pointer forward
                mid += 1  # Move the mid pointer forward

            # If the current element is 1, just move the mid pointer forward
            elif nums[mid] == 1:
                mid += 1

            # If the current element is 2, swap it with the element at the high pointer
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # Move the high pointer backward