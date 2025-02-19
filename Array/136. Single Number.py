"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space. 

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
import functools
import operator

class Solution:
  def singleNumber(self, nums: list[int]) -> int:
    # Use the XOR operator to find the single number
    # XOR of a number with itself is 0, and XOR of a number with 0 is the number itself
    return functools.reduce(operator.xor, nums, 0)