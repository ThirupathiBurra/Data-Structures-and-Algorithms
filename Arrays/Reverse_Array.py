""""
Quetsion : Reverse an array

You are given an array of integers arr[]. Your task is to reverse the given array.

"""
class Solution:
    def ReverseArray(self, arr):
        if not arr:
            return []
        for i in range(len(arr)):
            if i >= len(arr) - i - 1:
                break
            arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]

        return arr
#Example 

if __name__ == "__main__":
    solution = Solution()
    arr = [1,2,3,4,5]
    reversed_arr = solution.ReverseArray(arr)
    print(f"Reversed Array: {reversed_arr}")
    