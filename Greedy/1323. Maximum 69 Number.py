"""
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the number to a string for easy manipulation
        string = str(num)
        
        # Initialize an empty list to store the digits
        arr = []

        # Append each character (digit) from the string to the list
        for i in string:
            arr.append(i)
        
        # Iterate through the list of digits
        for i in range(len(arr)):
            # If the current digit is '6', replace it with '9' and break the loop
            if arr[i] == '6':
                arr[i] = '9'
                break
        
        # Join the list of characters back into a string
        modified_string = ''.join(arr)

        # Convert the modified string back to an integer
        modified_num = int(modified_string)

        # Return the modified number
        return modified_num