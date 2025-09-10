"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]




My reflection : Here we are checking the combination where the number can be used only once (at the index it is present).
                    From index starting to end (len(num)-1).
                    If the element is same as the previous one, we have to skip it.
                    
"""
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        candidates.sort()


        def findCombination(ind: int, target: int):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i + 1, target - candidates[i])
                ds.pop()


        findCombination(0, target)
        return ans
                
#Example
if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    obj = Solution()
    print(obj.combinationSum2(candidates,target))