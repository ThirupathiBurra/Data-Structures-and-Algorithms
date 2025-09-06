"""
leetcode 8:  String to Integer (atoi)

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


"""


""""
Here we need to do following :

1. Remove the leading spaces
2. Check if the string is positive or negative
    2.1 if it is negative then make a negative number
3. Round the number 
    3.1 if it is less than -2**31
        3.1.1 return -2**31
    3.2 if it is greater than 2**31-1
        3.2.1 return 2**31-1
4. Return the number
"""


class Solution:
    def myAtoi(self, s: str):

        if not s:
            return 0
        
        #Skipping the leadingspaces
        
        i = 0
        n = len(s)

        while i<n and s[i] == " ":
            i+=1

        if i == n:
            return 0
        
        #Sign checking
        sign = 1
        if s[i] == "+":
            sign = 1
        if s[i] == "-":
            sign = -1
            i += 1

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        res = 0
        while i<n and s[i].isdigit():
            digit = int(s[i])
            res = res*10+digit

            if sign*res <= INT_MIN:
                return INT_MIN
            if sign*res >= INT_MAX:
                return INT_MAX
            i+=1

        return res*sign



