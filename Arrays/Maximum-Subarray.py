""" 
Leetcode 53 : Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.


Kadane's algorithm to find the maximum subarray sum

Time Complexity : O(n)
Space Complexity: O(1)


def max_subarray_sum(arr):
    #Edge case 
    if not arr:
         return 0 
    current_sum = max_sum = arr[0]
    for num in arr[1:]:
        current_sum = current_sum + num
        max_sum = max(max_sum, current_sum)
    return max_sum
    

"""



class Solution:
    def max_sum_subarray(self,arr):
        if not arr:
            return 0
        current_sum = max_sum = 0
        for num in arr:
            current_sum = current_sum+ num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum

# Example
if __name__ == "__main__":
    solution = Solution()
    arr = [2, 3, -8, 7, -1, 2, 3]
    result = solution.max_sum_subarray(arr)
    print(f"Maximum subarray sum: {result}")

        