"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to eliminate duplicates
        set_1 = set(nums1)
        set_2 = set(nums2)
        # Initialize an empty list to store the intersection result
        ans = []

        # Iterate through each element in the first set
        for i in set_1:
            # Check if the element exists in the second set
            if i in set_2:
                # Append the element to the result list
                ans.append(i)
        
        # Return the list containing the intersection of the two sets
        return ans