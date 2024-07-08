'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
 nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

class Solution:
    def productExceptSelf(cls,nums):
        n= len(nums)
        res=[]
        if 0 in nums:
            if nums.count(0) > 1:
                return [0 for _ in nums]
            else:
                index = nums.index(0)
                product=1
                for i in nums:
                    if i!=0 : product *= i
                    res.append(0)
                res[index] = product
        else :
            product=1
            for i in nums:product*=i
            for k in nums : res.append(product//k)

        return res