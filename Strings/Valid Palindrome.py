"""
leetcode 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
        s = s.lower()
        n = len(s)
        l = 0
        r = n-1
        while l <= r:
            if not s[l].isalnum():
                l +=1
            elif not s[r].isalnum():
                r -=1
            else:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
        return True
        
        cleaned_string = ''.join([char for char in s.lower() if char.isalnum()])
        return cleaned_string == cleaned_string[::-1]
    
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)