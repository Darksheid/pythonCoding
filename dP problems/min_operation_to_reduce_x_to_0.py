'''
QUESTION :: Leetcode 1658. Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x. In one operation,
you can EITHER REMOVE THE LEFTMOST OR THE RIGHTMOST ELEMENT from the array nums and subtract its value from x.
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first
two elements (5 operations in total) to reduce x to zero.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
'''
#WA
def count(nums,x,l,r,c):
        if x==0 : return count
        elif x<0 : return float('inf')
        elif nums[l]> x and nums[r]<=x :
                return count(nums, x - nums[r], l, r - 1, c + 1)
        elif nums[l] > x and nums[r] <= x:
                return count(nums, x - nums[l], l+1, r, c + 1)
        elif nums[l]<=x and nums[r]<=x:
                min (count(nums, x - nums[r], l, r - 1, c + 1) , count(nums, x - nums[l], l+1, r, c + 1)  )

#WA for the below case
nums = [6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,
        765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119]
x = 31841
nums=[1,1,4,2,3]
x=5
l=0
r=4
c=0
print(count(nums,x,l,r,c))
