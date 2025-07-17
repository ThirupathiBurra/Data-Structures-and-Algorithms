"""

leetcode 42: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


 observation:
    - It can be solved by using this 'min(lmax,rmax)-height[i]' formula.
        - it can be used in all approaches.
    - We have to use two pointers, one from left to right and one from right to left.
    
    
    Time Complexity : O(n)
    Space Complexity : O(1)
    
 """

class Solution:

    def trap(self,height):

        l , r = 0,len(height)-1
        lmax , rmax = 0 ,0
        ans = 0
        while l < r:

            lmax = max(lmax,height[l])
            rmax = max(rmax,height[r])

            if lmax < rmax:
                ans += lmax-height[l]
                l += 1
            else:
                ans += rmax-height[r]
                r -= 1
        return ans

#Example
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    result   = solution.trap(height)
    print(result)