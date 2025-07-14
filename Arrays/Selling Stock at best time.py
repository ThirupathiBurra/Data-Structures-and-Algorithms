"""
leetcode 121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



My reflection :
    First we have find the min value before going to calculate the profit by iterating comapring.

    Calculating the profit as in a processes we compare and store the max and that we return.


"""
class Solution:
    def Best_Time_to_Buy_and_Sell_Stock(self,arr):
        max_profit, min_value= 0 , arr[0]
        for i in range(1,len(arr)):
            max_profit = max(max_profit,(arr[i]-min_value))
            min_value = min(min_value,arr[i])
        return max_profit

#Example 
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    result = solution


