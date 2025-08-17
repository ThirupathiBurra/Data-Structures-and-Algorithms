"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self,s):

        #Edge Case
        if not s:
            return ""
        
        prefix = s[0]
        for s in s[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix

#   Time Complexity : O(n)
#   Space Complexity : O(1)
if __name__ == "__main__":
    s = ["flower","flow","flight"]
    solution = Solution()
    result = solution.longestCommonPrefix(s)
    print(result)

    