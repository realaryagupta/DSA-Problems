
# Find the repeating and missing number

"""
Given an integer array nums of size n containing values from [1, n] and each value appears 
exactly once in the array, except for A, which appears twice and B which is missing.

Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

Input: nums = [3, 5, 4, 1, 1]
Output: [1, 2]
Explanation: 1 appears two times in the array and 2 is missing from nums

Input: nums = [1, 2, 3, 6, 7, 5, 7]
Output: [7, 4]
Explanation: 7 appears two times in the array and 4 is missing from nums.
"""

# solved on 19 June 2025 by Arya Gupta
nums = [1, 2, 3, 6, 7, 5, 7]  # Example: 4 is missing, 7 is duplicated

def findMissingRepeatingNumbers(nums):
    n = len(nums)
    hashset = set(nums)
    
    # Find the duplicate
    nums_sum = sum(nums)
    set_sum = sum(hashset)
    duplicate_number = nums_sum - set_sum

    # Find the missing number
    # Expected sum if all numbers from 1 to n are present
    expected_sum = n * (n + 1) // 2
    # Sum of unique numbers in the array
    unique_sum = set_sum
    # Missing number is expected_sum - unique_sum
    missing_number = expected_sum - unique_sum

    return [duplicate_number, missing_number]

print(findMissingRepeatingNumbers(nums))