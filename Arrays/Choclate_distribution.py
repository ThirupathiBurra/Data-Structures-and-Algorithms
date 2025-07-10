"""
GeekForGeeks
Question:   Chocolate Distribution Problem

Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
    i. Each student gets exactly one packet.
    ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.

    

Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
Output: 6
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following m packets :[3, 4, 9, 7, 9].
"""

"""My reflection : 
    The array of size "m" of elements. The differnece of minimum value of the "m" sized aray and maximum value of "m" sized array should be minimum.
    So, we need a subset's of size "m" , the difference's of max and min value's of all subsets should be minimum  among all.
"""

class Solution:
    def Chocolates_disribution(self,arr,m):

        #Sort the array to get a subset which comes from the sorted subarrays
        if len(arr) < m:
            return -1
        minimum_diff= diff= float('inf')
        arr.sort()
        #Iterate over the array and find the minimum difference
        for i in range(len(arr)-m+1):
            diff = arr[m-1+i] - arr[i]
            minimum_diff = min(minimum_diff,diff)
        return minimum_diff
    
# Example
if __name__ == "__main__":
    arr = arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    arr1 = [11,13,7,5,13,12]
    m1 = 4
    solution = Solution()
    result = solution.Chocolates_disribution(arr,m)
    result1 = solution.Chocolates_disribution(arr1,m1)
    print(f"Minimum difference is {result}")
    print(f"Minimum difference is {result1}")
    
            


