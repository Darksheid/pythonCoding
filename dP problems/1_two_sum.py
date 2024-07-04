'''
Two Integer Sum
Given an array of integers nums and an integer target,
return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

Solution : take a dict ,store nums values as keys against index as value,then check if target - values in the dict
if not store it, if present then return the value
As there is only one solution , and there is no case for no solution
'''

def twoSum(nums,target):
    dp={}
    for i,n in enumerate(nums):
        diff= target- n
        if diff in dp : return [dp[diff],i]
        dp[n] = i

nums=[4,5,6]
target=10
print(twoSum(nums,target))
