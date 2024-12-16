"""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. 
If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer. 

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
"""

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Convert the input lists into sets to eliminate duplicates and enable set operations
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of the two sets to get common elements
        common_elements = set1.intersection(set2)
        
        # If there are common elements, return the smallest one
        if common_elements:
            return min(common_elements)
        else:
            # If there are no common elements, return -1
            return -1