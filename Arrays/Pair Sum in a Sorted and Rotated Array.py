"""
Given an array of positive elements arr[] that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with sum equals to a given target.

Examples:

Input: arr[] = [7, 9, 1, 3, 5], target = 6
Output: true
Explanation: arr[2] and arr[4] has sum equals to 6 which is equal to the target.
Input: arr[] = [2, 3, 4, 1], target = 3
Output: true
Explanation: arr[0] and arr[3] has sum equals to 3 which is equal to the target.
Input: arr[] = [10, 7, 4, 1], target = 9
Output: false
Explanation: There is no such pair exists in arr[] which sums to target.

"""

class Solution:
    def PairSum(self,arr,target):
        l, r = 0, len(arr)-1
        i=0

        for i in range(len(arr)):

            if arr[i] > arr[i+1]:
                i = i + 1
                break
        # if arr[i] > arr[i+1]:
        #     i = i+1
        
        r = i
        l = (i+1)%len(arr)

        while l != r:
            if arr[l] + arr[r] == target:
                return True
            elif arr[l] + arr[r] < target:
                l = (l+1)%len(arr)
            else:
                r = (r-1)%len(arr)
        return False
    
#Example
if __name__ == '__main__':
    arr = [7, 9, 2, 3, 5]
    target = 7
    obj = Solution()
    print(obj.PairSum(arr,target))