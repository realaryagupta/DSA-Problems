"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Get the length of the input list
        n = len(nums)
        # If the list is empty, return 0
        if n == 0:
            return 0

        # Initialize the longest sequence length to 1
        longest = 1
        # Create a set to store all the numbers for O(1) lookup
        st = set()
        
        # Add all elements of the list to the set
        for i in range(n):
            st.add(nums[i])

        # Iterate through each number in the set
        for it in st:
            # Check if the current number is the start of a sequence
            if it - 1 not in st:
                # Initialize a counter for the current sequence
                cnt = 1
                x = it
                # Find the length of the consecutive sequence
                while x + 1 in st:
                    x += 1
                    cnt += 1
                # Update the longest sequence length if the current sequence is longer
                longest = max(longest, cnt)
        
        # Return the length of the longest consecutive sequence
        return longest