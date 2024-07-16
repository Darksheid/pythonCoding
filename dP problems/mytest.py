



def maxSubarraySumCircular(nums):
    max_n = max(nums)
    if max_n < 0: return max_n

    for i in range(len(nums)):
        arr = nums[i:] + nums[:i]
        print(arr)
        max_n = max(kadane(arr), max_n)
    return max_n


def kadane(arr):
    currSum = 0
    maxSum = 0

    for n in arr:
        currSum += n
        currSum = max(currSum, n)
        maxSum = max(maxSum, currSum)
    return maxSum



nums = [2,3,-2,1,-4]
print(maxSubarraySumCircular(nums))


