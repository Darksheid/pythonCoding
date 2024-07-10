'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
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


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104

Solution :
 Please draw a line plot to visualize the problem

 Brute force : O(n^2) : We can take all the combinations and take the max value of profit

 Optimal Solution O(n) Time complexity with few extra spaces 0(1) space complexity
 lets take two pointers , l,r and start from beginning of the prices array
 l,r = 0,1
1>>So we buy at l and sell at r posn because we can buy earlier and sell later
2>>When we encounter prices[r]< =prices[l] we make l=r so that the buying price becomes lowest, and increase the r by 1
3>>When we encounter prices[r]> prices[l] we factor that into the solution by taking the
  max between previous maxprice and prices[r]-prices[l] and increase the r by 1

4>>Continue the loop till r=prices.length
'''

def getmaxprofit(prices):
    n=len(prices)
    maxprofit=0
    l,r = 0,1
    while r<n:
        if prices[r]> prices[l]:
           maxprofit = max(maxprofit,prices[r]-prices[l])
        else:
            l=r
        r+=1
    return maxprofit

prices = [7,1,5,3,6,4]
print(getmaxprofit(prices))


