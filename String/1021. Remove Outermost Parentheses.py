'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Initialize an empty string to store the result
        res = ""
        # Initialize a counter to track the balance of parentheses
        count = 0
        
        # Iterate through each character in the input string
        for char in s:
            # Case 1: If the character is '(' and count is 0, it means this is the outermost '('
            # We do not add it to the result, just increment the count
            if char == '(' and count == 0:
                count += 1
            
            # Case 2: If the character is '(' and count is 1 or more, it means this is an inner '('
            # We add it to the result and increment the count
            elif char == '(' and count >= 1:
                res += char
                count += 1
            
            # Case 3: If the character is ')' and count is greater than 1, it means this is an inner ')'
            # We add it to the result and decrement the count
            elif char == ')' and count > 1:
                res += char
                count -= 1
            
            # Case 4: If the character is ')' and count is 1, it means this is the outermost ')'
            # We do not add it to the result, just decrement the count
            elif char == ')' and count == 1:
                count -= 1
        
        # Return the final result after processing the entire string
        return res