'''
0/1 Knapsack problem:
You are provided arrays in profit and weight of each item.
Say for Example wt = [3, 2, 4] ; profit = [6, 8, 7]
for item1 wt is 3 and its price/profit = 6
Given a bag/Knapsack ,with max capacity w, where you can select the item to keep in the bag,
or you did not select the item
You cannot partially select the item to be placed in the bag

You need to determine what is the max profit you can make by selecting items to be kept in the knapsack.
For the above example
wt = [3, 2, 4] ; profit = [6, 8, 7] ,w=8
Maxprofit will be made when items with wt 2,4 and profit 8,7 is selected , which is 15
'''

#Recursive Solution
# Time Complexity O(n2) :   Either we select or we don't select the item
# Space Complexity O(n) :   Memory from Stack is utilized to store the recursive call values,
#                           May run into Stack overflow.
def knapsack(w, n):
    if w == 0 or n == 0:
        return 0
    elif wt[n - 1] > w:
        return knapsack( w, n - 1)
    else:
        return max(knapsack( w, n - 1),
                   knapsack( w - wt[n - 1], n - 1) + profit[n - 1])

#DP Solution
# Time Complexity O(n.w) :  Either we select or we don't select the item
# Space Complexity O(n.w) : Memory from heap is utilized to store dp matrix values
def knapsackDP(wt, profit, w, n):
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + profit[i - 1])
    return dp[n][w]


wt = [3, 2, 4]
profit = [6, 8, 7]
w = 8
n = len(wt)
print(knapsack(w,n))
#print(knapsackDP(wt, profit, w, n))
