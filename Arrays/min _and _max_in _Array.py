""""
Question :Min and Max in Array

Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

"""


class Solution:
    def min_and_max_in_array(self,arr):
        if not arr: #Edge case for empty array
            return None, None
        min_value = max_value = arr[0]
        for num in arr[1:]:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num
        return min_value, max_value

#Example 
if __name__ == "__main__":
    solution = Solution()
    arr = [3, 2, 1, 56, 10000, 167]
    min_value, max_value = solution.min_and_max_in_array(arr)
    print(f"Minimum value: {min_value}, Maximum Value: {max_value}")
    arr1 = []
    min_value, max_value = solution.min_and_max_in_array(arr1)
    print(f"Minimum value: {min_value}, Maximum Value: {max_value}")
