'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Solution :
 lets take nums =[1,2,4,3]
 IF only one element is present in the array then longest INCREASING Subsequence = 1
 Thus we make a DP array of Lenght nums and assign 1 to each element
 **What is the longest INCREASING Subsequence i.e LIS we make out of last element [3] = 1 => LIS[3] = 1
 **LIS[2] means LIS using [4,3] , (either we can take 4 and exclude everything) =>LIS[2] or (include 4 and 3)=> 1+LIS[3]
    and include maximum out of both.
    >>but if we include [4,3] in solution then the sequence no longer remains increasing, thus we have apply condition
        where nums[2]<nums[3] then lIS[2] = max( LIS[2] , 1+LIS[3])
**Similary , LIS[1] means LIS using [2,4,3]
            => LIS[1] = max(either we take only LIS[1] ,  take LIS[1] and LIS[2] , take LIS[1] and LIS[3] )
            =>LIS[1] = max(LIS[1],1+LIS[2],1+LIS[3])
**Similary LIS[0] means LIS using [1,2,4,3]
            =>LIS[0] = max(LIS[0], 1+LIS[1],1+LIS[2],1+LIS[3])

'''


def lengthOfLIS( nums) :
    '''
    Base case considering each element as the longest sequence
    '''
    LIS = [1 for _ in range(len(nums))]

    for i in range(len(LIS) - 1, -1, -1):
        for j in range(i + 1, len(LIS)):
            if nums[j] > nums[i]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))

nums = [0, 1, 0, 3, 2, 3]
print(lengthOfLIS(nums))

nums = [7, 7, 7, 7, 7, 7, 7]
print(lengthOfLIS(nums))