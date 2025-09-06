"""Recursion :

    resursion is a process of calling a fuction which contains a block of code of certain fuctionallities.


To implement recursion we use :
    1. Base case
    2. Recursive case (take and not take)
   """
 
 ## Subsequence problem

class Solution:
    def __init__(self):
        self.res = []
    def subsequence(self, ind , nums, ans):
        
        if ind == len(nums):
            self.res.append(ans.copy())
            return
        ans.append(nums[ind])
        self.subsequence(ind+1,nums,ans)
        ans.remove(nums[ind])
        self.subsequence(ind+1, nums,ans)
        return self.res
    def result(self,nums):
        ans = []
        return self.subsequence(0,nums,ans)
    
#Example
if __name__ == "__main__":
    nums = [3,1,2]
    solution = Solution()
    result = solution.result(nums)
    print(sorted(result))
            
