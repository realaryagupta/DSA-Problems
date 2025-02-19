'''
Check for Balanced Parentheses
Problem Statement: Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.
Note: string str is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: str = “( )[ { } ( ) ]”
Output: True
Explanation: As every open bracket has its corresponding 
close bracket. Match parentheses are in correct order 
hence they are balanced.

Example 2:
Input: str = “[ ( )”
Output: False
Explanation: As ‘[‘ does not have ‘]’ hence it is 
not valid and will return false.
'''

class Parenthesis:
    def isValid(self, s):
        st = []
        
        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                
                ch = st[-1]
                st.pop()
                
                # Check if the popped opening bracket matches the current closing bracket
                if (i == ")" and ch == "(") or (i == "}" and ch == "{") or (i == "]" and ch == "["):
                    continue  # Valid match, continue to next character
                else:
                    return False  # Mismatch found, return False
                
        # If the stack is empty at the end, all brackets were matched correctly
        return len(st) == 0