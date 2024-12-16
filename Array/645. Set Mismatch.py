"""
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
 

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Initialize an empty set to track seen numbers
        set_1 = set()
        # Initialize a variable to store the duplicate number
        duplicate = -1
        
        # Iterate through the list to find the duplicate
        for num in nums:
            if num in set_1:
                duplicate = num
            set_1.add(num)
        
        # Calculate the expected sum of numbers from 1 to n
        n = len(nums)
        total_sum = (n * (n + 1)) // 2
        
        # Calculate the actual sum of the given list
        actual_sum = sum(nums)
        
        # Calculate the missing number by subtracting the adjusted actual sum from the total sum
        missing = total_sum - (actual_sum - duplicate)
        
        # Return the duplicate and missing numbers
        return [duplicate, missing]