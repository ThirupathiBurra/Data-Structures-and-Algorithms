"""
Here we have to find the subsequence whose sum is equal to the sum of the array.
"""

class Solution:
    def __init__(self):
        self.res = []

    def Subsequence(self, ind, ans, nums, s, sum):
        
        if ind >= len(nums):
            if s == sum:
                self.res.append(ans.copy())
                return True
            return False
        
        ans.append(nums[ind])
        s = s+nums[ind]
        if self.Subsequence(ind+1, ans, nums, s, sum):
            return True
        
        s = s-nums[ind]
        ans.remove(nums[ind])

        if self.Subsequence(ind+1, ans, nums, s, sum):
            return True
        return False
    def result(self, nums, sum):
        ans = []
        self.Subsequence(0, ans, nums, 0, sum)
        return self.res
    

if __name__ == "__main__":
    nums = [3,1,2]
    sum = 0
    solution = Solution()
    result = solution.result(nums,sum)
    print(result)