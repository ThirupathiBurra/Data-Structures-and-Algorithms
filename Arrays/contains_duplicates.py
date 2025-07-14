"""
Leetcode 517 :Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
class Solution:
    def ContainsDuplicates (self,arr):
        s = list(set(arr))
        if len(arr) == len(s):
            return False
        return True
    
# Example
if __name__ == "__main__":
    arr = [1,2,3,1]
    solution = Solution()
    result = solution.ContainsDuplicates(arr)
    if result:
        print("Yes the array contains the duplicates")
    else:
        print("NO,The array does not contains any duplicates")


