'''
Max Water Container
You are given an integer array heights where heights[i] represents the height of the
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
#######################################################Solution#######################################################

BRUTE FORCE ( Time complexity O(n^2) ,Space Complexity O(1) )
We take all the possible combinations of 2 heights and get the max out of it.

Optimum Solution ( Time complexity O(n) ,Space Complexity O(1) )
We take Two pointers one at first and one at last,
(to capture the max volume as distance between first and last will be greatest)
l,r = 0 , n-1

###Now Check if heights[l]>heights[r] : then already the left value is greater than right, thus no point in leaving left pointer
        Thus we shift the right pointer to left => r=r-1
###Similarly if heights[l]<heights[r] : then we shift the left pointer to right => l=l+1
###if heights[l]==heights[r] : we can shift the left pointer to right vice versa

'''


def maxArea(heights):
    n = len(heights)
    l, r = 0, n - 1
    max_vol = 0

    while l < r:
        curr_vol = min(heights[l], heights[r]) * (r - l)
        max_vol = max(max_vol, curr_vol)
        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1
    return max_vol


height = [1,7,2,5,4,7,3,6]
print(maxArea(height))