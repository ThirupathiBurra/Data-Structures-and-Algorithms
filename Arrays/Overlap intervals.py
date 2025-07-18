""""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def mergeOverlap(arr):
    n = len(arr)

    arr.sort()
    res = []

    # Checking for all possible overlaps
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        # Skipping already merged intervals
        if res and res[-1][1] >= end:
            continue

        # Find the end of the merged range
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])
    
    return res

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for interval in res:
        print(interval[0], interval[1])


class Solution:
    def merge(self, arr) :
        arr.sort()
        res = []
        res.append(arr[0])

        for i in range(1,len(arr)):
            last = res[-1]
            curr = arr[i]

            if curr[0] <= last[1]:
                last[1] = max(last[1],curr[1])
            else:
                res.append(curr)
        return res

#Example
if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    solution = Solution()
    result = solution.merge(arr)

    print(result)
