'''
918. Maximum Sum Circular Subarray
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element
of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once.
Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
##########################################################Solution####################################
Brute Force (Time complexity O(n2)):
Take all combinations of circular array say if nums = [1,-2,3,2], then possible combinations are
[1,-2,3,2], [-2,3,2,1] , [3,2,1,-2] , [2,1,-2,3]
use kadane algo in all the arrays and get the maxSum

Optimized(TC O(n)):
lets say arr = [3,2,1,-2] ,
1>maxSumSubArray value will be found using Kadane,
2>we also find the minSumSubArray using the same Kadane Algo
3>Now, the subarraySum without the minSumSubarray = Total Sum of array - minSumSubArray,
This above calculated subarray potentially(if taken as S set) has the maxsumSubArray(Actual result) or
maxsumSubArray(calcuated in Kadane Algo) from Step 1(take as subset of S)
We need to take the max of both the values

###Edge case when all the elements are negative, then maxsumSubArray will be negative,
thus in this case we need to return the maxsumSubArray derived from kadane Algo###


'''


def maxSubarraySumCircular(nums):
    maxSum, minSum = nums[0], nums[0]
    currMaxSum, currMinSum = 0, 0
    total = 0

    for n in nums:
        currMaxSum = max(currMaxSum + n, n)
        currMinSum = min(currMinSum + n, n)
        total += n
        maxSum = max(maxSum, currMaxSum)
        minSum = min(minSum, currMinSum)
    return max(total - minSum, maxSum) if maxSum > 0 else maxSum

nums = [5,-3,5]
print(maxSubarraySumCircular(nums))
