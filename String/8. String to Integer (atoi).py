"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^

Example 5:
Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.
"""

import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing spaces
        
        if not s:
            return 0  # Handle empty string

        # Initialize sign
        String_Sign_True_Counter = True

        # Check the first character for sign
        if s[0] == "-":
            String_Sign_True_Counter = False
            s = s[1:]  # Remove the sign for further processing
        elif s[0] == "+":
            String_Sign_True_Counter = True
            s = s[1:]  # Remove the sign for further processing
        elif not re.match(r'^[0-9]', s[0]):
            return 0  # If the first character is not a digit, return 0

        # Match the numeric part of the string
        match = re.match(r'^\d+', s)
        
        if match:
            # Extract the matched numeric part
            string_2 = match.group(0)
            
            # Convert the extracted part to an integer
            result = int(string_2)
            
            # Apply the sign
            if not String_Sign_True_Counter:
                result = -result
            
            # Clamp the result to fit within the 32-bit integer range
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31
            
            if result > INT_MAX:
                return INT_MAX
            elif result < INT_MIN:
                return INT_MIN
            
            return result
        else:
            return 0
