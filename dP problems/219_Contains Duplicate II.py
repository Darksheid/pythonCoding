'''
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''


def containsNearbyDuplicate(nums, k):
    mapdict = {}
    for i, v in enumerate(nums):
        if v in mapdict and i - mapdict[v] <= k:
            return True
        mapdict[v] = i
    return False

nums=[1,2,3,1,2,3]
k=3
print(containsNearbyDuplicate(nums, k))