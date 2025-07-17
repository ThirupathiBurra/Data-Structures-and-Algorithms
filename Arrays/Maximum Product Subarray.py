"""
152. Maximum Product Subarray
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

class Solution:
    def maxProduct(self, nums):
        max_product = max(nums)
        s = 1
        l = len(nums)
        for i in range(0,l):
            s = s*nums[i]
            max_product = max(max_product,s)
            if s==0:
                s = 1
        s = 1
        for i in range(l-1,-1,-1):
            s = s*nums[i]
            max_product = max(max_product,s)
            if s==0:
                s = 1  
        return max_product

#Example
if __name__ == "__main__":
    nums = [2,3,-2,4]
    solution = Solution()
    result = solution.maxProduct(nums)
    print(result)