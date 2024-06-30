'''
Cutting a Rod | DP-13

Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

For example 1,
if the length of the rod is 8 and the values of different pieces are given as the following,
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

For example 2
And if the prices are as follows, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
'''


def getmaxvalue(price, n):
    dp = [[0 for _ in range(1 + n)] for _ in range(1 + n)]
    arr=[ k for k in range(1,1+n)]
    for i in range(1,1+n):
        for j in range(1,1+n):
            if arr[i-1]>j : dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = max(dp[i-1][j] , dp[i][j-arr[i-1]] + price[i-1])
    return dp[n][n]

price =[1,5,8,9,10,17,17,20]
n=len(price)
print(getmaxvalue(price, n))


price =[3,5,8,9,10,17,17,20]
n=len(price)
print(getmaxvalue(price, n))
