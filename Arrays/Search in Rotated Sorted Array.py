"""
leetcode 33 : Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


My reflection : 
    The left half of the array is always sorted , so we can use the Binary search on the list.
"""

class Solution:
    def Search_in_Roated_array(self,arr,target):
        low, high = 0 , len(arr)-1

        while low <= high:
            mid = (low+high)//2

            #Checking the target at mid
            if target == arr[mid]:
                return mid
            
            #Checking the left half first
            elif arr[low] <= nums[mid]:
                #checking wheather the element is present or not
                if arr[low] <= target and target <= arr[mid]:
                    high = mid-1
                else:
                    low = mid+1

            #Checking the element in the right half
            else:
                if arr[mid] <= target and target <= arr[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

#Example 
if __name__ == "__main__":
    solution = Solution()
    arr = nums = [4,5,6,7,0,1,2]
    target = 0
    result = solution.Search_in_Roated_array(arr,target)
    if result == -1:
        print("Target not there in the array")
    else:
        print(f"The target found at index {result}")