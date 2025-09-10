"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

"""
"""
My reflection : In this we have to make the 3 choices for each index, so that we can get the combinations.
                    we should pisk an element at once and twice or we should not pick it at all. 
                
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []


        def findCombination(ind: int, target: int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findCombination(ind, target - candidates[ind])
                ds.pop()
            findCombination(ind + 1, target)
        findCombination(0, target)
        return ans
    

# Example
if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    obj = Solution()
    print(obj.combinationSum(candidates,target))