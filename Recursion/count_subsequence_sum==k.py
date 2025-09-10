"""

here we are counting the sum of the subsequence whose sum is equal to the given k value.

"""

class Solution:
    def __init__(self):
        self.res = []

    def Subsequence_count(self, ind, ans, nums, sum, k):
        if ind >= len(nums):
            if sum == k:
                return 1
            return 0
        sum = sum+nums[ind]
        l = self.Subsequence_count(ind+1, ans, nums, sum, k)
        sum = sum-nums[ind]
        r = self.Subsequence_count(ind+1, ans, nums, sum, k)
        return l+r
    
    def result(self, nums, k):
        ans = []
        return self.Subsequence_count(0, ans, nums, 0, k)

#Example
if __name__ == "__main__":
    nums = [3,1,2]
    k=2
    solution = Solution()
    result = solution.result(nums,k)
    print(result)