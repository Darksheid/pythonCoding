'''
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

Solution:
for every sequence starting we can see that the num(starting sequence number) - 1 exists or not
if exists then check the next value is present or not and continue till next value don't exist
if next value don't exist, stop counting
need to get the max of previous calculated max length to current sequence length
'''


def longestConsecutive(nums):
    maxcount = 0
    set_nums = set(nums)
    for i in set_nums:
        if i - 1 not in set_nums:
            curr_count = 0
            while i + curr_count in set_nums:
                curr_count += 1
            maxcount = max(maxcount, curr_count)
    return maxcount
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(set(nums))
print(longestConsecutive(nums))