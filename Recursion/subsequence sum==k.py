"""
Recursion problem 
 Here we need to find the subsequence sum == k

"""

class Solution:
    def __init__(self):
        self.res = []
    
    def Subsequence(self, ind, ans, nums, sum, k):

        if(ind >= len(nums)):
            if(sum == k):
                self.res.append(ans.copy())
            return
        
        #Pick the current
        ans.append(nums[ind])
        sum = sum+nums[ind]
        self.Subsequence(ind+1, ans, nums, sum, k)

        sum = sum-nums[ind]
        ans.remove(nums[ind]) #Backtrack

        #Not picking the current
        self.Subsequence(ind+1, ans, nums, sum, k)
        return self.res

    def result(self, nums, k):
        ans = []
        return self.Subsequence(0, ans, nums, 0, k)
    
#Example
if __name__ == "__main__":
    nums = [3,1,2]
    k=3
    solution = Solution()
    result = solution.result(nums,k)
    print(result)

