'''
983. Minimum Cost For Tickets
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.

'''



def mincostTicketsMemo(days,costs):
        dp = {}

        def dfs(i):
            # base case when there is no days left to traverse no cost is added hence 0 returned
            if i == len(days):
                return 0
            # if value of i is already calculated then we reuse the value from dp memo
            if i in dp:
                return dp[i]
            # dp[i] is set to max value possible, need to get the min value
            dp[i] = float('inf')

            for d, c in zip([1, 7, 30], costs):

                # actual code should look like this,dp[i] = min(dp[i], c+dfs(i+d)) but need to calculate the d first
                # check the case for costs : [1,2,8] and d=7
                ##Increment j value such that the loop stops at the point  where we can get the next value
                # of day from days array providing days[j]<(=)days[i] + d , (=) will over shoot the
                # days value by one position

                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1

                dp[i] = min(dp[i], c + dfs(i + j))

            # return dp[i] value for the dfs(i) function
            return dp[i]

        # return dfs(starting from first element : 0)  to the main function
        return dfs(0)

def mincostDP(days,costs):
    dp={}
    for i in range (len(days)-1,-1,-1):
        dp[i] = float('inf')
        for d, c in zip([1, 7, 30], costs):
            j = i
            while j < len(days) and days[j] < days[i] + d:
                j += 1
            dp[i] = min(dp[i], c + dp.get(j,0))
            #dp.get(j,0) is hashmap function of python handle the case if j==len(days) return 0
    return dp[0]

days=[1,4,6,7,8,20]
costs=[2,7,15]
print(mincostDP(days,costs))
#DP one is the accepted code