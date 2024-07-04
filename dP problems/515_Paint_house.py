
'''
515 · Paint House
Description
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
 The cost of painting each house with a certain color is different.
 You have to paint all the houses such that no two adjacent houses have the same color,
 and you need to cost the least. Return the minimum cost.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2]
is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
'''
def findmincost(cost):
    c=len(cost[0])
    r=len(cost)
    '''
    Take a DP table where 
    **dp[1][0] represents if we paint 2nd house with 1st house with 1st color i.e. red, then what is the min cost
    **dp[1][1] represents if we paint 2nd house with 1st house with 2nd color i.e. blue, then what is the min cost
    And so on...
    initially all values are set to 0
    '''
    dp=[[0 for _ in range(c)] for _ in range(r)]

    '''
    Base case to paint the first house either red,blue,green is same as individual cost of the color for 1st house
    '''
    dp[0] = cost[0]
    '''
    Lets say we are now at 2nd house, and selected red to be color of 2nd house, that means that we have choose either
    **house1 colour to be blue or it can be green, we need to take the min of both costs and add to the cost house2 red
    thus to paint house 2 red will be :
        cost[1][0] + min(cost to paint house 1 blue , cost to paint house 1 green)
        cost to paint house 1 blue , cost to paint house 1 green both values are saved in DP table as dp[0][1],dp[0][2]
        thus value becomes 
        cost[1][0] + min(dp[0][1],dp[0][2]) , we need to save it in dp[i][j]
        
        Similarly calculate the values for Blue and Green
    
    '''
    for i in range(1,r):
        for j in range(c):
            if j==0 :
                dp[i][j] = cost[i][j] + min(dp[i-1][1],dp[i-1][2])
            elif j==1 :
                dp[i][j] = cost[i][j] + min(dp[i - 1][0], dp[i - 1][2])
            else:
                dp[i][j] = cost[i][j] + min(dp[i - 1][0], dp[i - 1][1])
    print(dp)
    '''
    Finally we need to take the min value among cost to paint house nth as red,blue and green
    '''
    return (min( dp[r-1] ))
cost= [[14,2,11],[11,14,5],[14,3,10]]
print(findmincost(cost))
'''Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
'''