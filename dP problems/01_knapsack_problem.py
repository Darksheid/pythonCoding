def knapsack(wt,profit,w,n):
    if w==0 or n==0 : return 0
    elif wt[n-1]>w : return knapsack(wt,profit,w,n-1)
    else :
        return max(knapsack(wt,profit,w,n-1) ,
                   knapsack(wt,profit,w-wt[n-1],n-1) + profit[n-1])

def knapsackDP(wt,profit,w,n):
    dp=[[0 for _ in range (w+1) ] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]>j : dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-wt[i-1]] + profit[i-1])
    return dp[n][w]

wt=[3,2,4]
profit=[6,8,7]
w=8
n=len(wt)
#print(knapsack(wt,profit,w,n))
print(knapsackDP(wt,profit,w,n))
