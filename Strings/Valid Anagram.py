"""
leetcode 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""

class Solution:
    def ValidAnagram(self, s,t):
        if len(s) != len(t):
            return False
        
        S = set(s)
        for c in S:
            if s.count(c) != t.count(c):
                return False
        else:
            return True
        
# Time Complexity : O(n)
# Space Complexity : O(n)

# Example
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    result = solution.ValidAnagram(s,t)
    print(result)