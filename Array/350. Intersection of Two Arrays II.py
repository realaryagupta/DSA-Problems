"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
 

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize an empty list to store the intersection result
        res = []

        # Iterate through each number in the first list
        for num in nums1:
            # Check if the number exists in the second list
            if num in nums2:
                # Append the number to the result list
                res.append(num)
                # Remove the number from the second list to handle duplicates
                nums2.remove(num)
        
        # Return the list containing the intersection of the two lists
        return res