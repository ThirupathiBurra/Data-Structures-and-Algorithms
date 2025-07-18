"""
K’th Smallest Element in Unsorted Array

Given an array arr[] of N distinct elements and a number K, where K is smaller than the size of the array. Find the K'th smallest element in the given array.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
Output: 10 

"""
import heapq
class Solution:
    def kthsmallest(self,arr,k):
        max_heap = []

        for num in arr:

            heapq.heappush(max_heap, -num)

            if len(max_heap) > k:
                heapq.heappop(max_heap)

            return -max_heap[0]
        
# Time Complexity : O(nlogk)
# Space Complexity : O(k)

#Example
if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    solution = Solution()
    result = solution.kthsmallest(arr,k)
    print(result)