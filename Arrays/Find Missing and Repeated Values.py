"""2965. Find Missing and Repeated Values

You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

My reflection :
    - First i thought it could be easy to sort and return the len(nums)-k, which gives T.C : O(nlogn)
    - min heap could be the another approact with T.C : O(nlogk) & S.C : O(k)
    - Quick select is one among them which is best in average case with T.C : O(n) & S.C : O(1)
"""

"""
    # Quick Select algo

"""
import heapq
class Solution:
    def kthLargest(self,nums,k):

        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
    
# Time Complexity : O(nlogk)
# Space Complexity : O(k)

# Example

if __name__ == "__main__":
    arr = [3,2,1,5,6,4]
    k = 2
    solution = Solution()
    result = solution.kthLargest(arr,k)
    print(result)