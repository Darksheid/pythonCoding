'''
322. Coin Change
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''


def changeRecursive(coins,amt,n):
    if amt==0 and n==0 : return 0
    elif amt>0 and n==0 : return float('inf')
    elif coins[n-1]>amt :
        return changeRecursive(coins,amt,n-1)
    else:
        return min(changeRecursive(coins,amt,n-1),
                   1+changeRecursive(coins,amt-coins[n-1],n))
#coin change 1 solution
def getmincoinsDP(coins,amt,n):
    dp=[[ 0 if k==0 else float('inf') for k in range(1+amt)] for _ in range(1+n)]
    for i in range(1,n+1):
        for j in range(1,amt+1):
            if coins[i-1]>amt : dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j] , 1+dp[i][j-coins[i-1]])
                
    return dp[n][amt] if dp[n][amt]!=float('inf') else -1

def countwaystogetTarget(coins,amt,n):
    dp=[[ 1 if k==0 else 0 for k in range(1+amt)] for _ in range(1+n)]
    for i in range(1,n+1):
        for j in range(1,amt+1):
            if coins[i-1]>amt : dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    return dp[n][amt]
    

coins=[1,2,5]
amt=5
n=len(coins)
#print(getmincoinsDP(coins,amt,n))
print(countwaystogetTarget(coins,amt,n))
