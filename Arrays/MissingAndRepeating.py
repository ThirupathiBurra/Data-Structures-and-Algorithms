
""""
2965. Find Missing and Repeated Values

You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
"""



class Solution:
# Python program to find Missing 
# and Repeating in an array

    def findTwoElement(self,arr):
        n = len(nums)
        
        repeating = -1
    
        for i in range(n):
            val = abs(nums[i])
    
            if nums[val - 1] > 0:
                nums[val - 1] = -1 * nums[val - 1]
            else:
                
                # Element is repeating.
                repeating = val
    
        missing = -1
    
        # Value at missing value index
        # will be positive.
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
    
        return [repeating, missing]

if __name__ == "__main__":
    nums = [2, 1,3, 3]
    solution = Solution()
    print(solution.findTwoElement(nums))