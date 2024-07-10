'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
##########################################################################################################
Solution Optimal O(n^2) time complexity  , space complexity O(n):
Here the elements can repeat any number of times

####lets say the if the elements are not repeating, then its basically a 2 sum solution
with another element we can pass via a loop ,Solution is as follows:

def threeSum(nums):
        res=[]
        nums.sort() # to implement 2 sum with sorted list
        for i,a in enumerate(nums):
            l,r = i+1,len(nums)-1
            while l<r:
                triplets = a+nums[l]+nums[r]
                if triplets>0:r-=1
                elif triplets<0:l+=1
                else:
                    res.append([a,nums[l],nums[r]])
        return res

If we implement the above solution , then we will get duplicate triplets, which have to be ignored
Lets take a sorted list [-4,-1,-1,0,1,2] , lets take i,j,k = 1,3,4 and i,j,k = 2,3,4 both are solutions
but are basically same triplets, thus while selecting i if the next element is same as the previous element
we basically have to ignore the next value

This problem will also occur while choosing the l, r pointers for 2 sum


'''

def threeSum(nums):
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            '''
            While selecting i if the next element is same as the previous element
            we basically have to ignore the next value, as the combination is 
            already considered in solution set
            '''
            if i>0 and nums[i-1]==a:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                triplets = a+nums[l]+nums[r]
                if triplets>0:r-=1
                elif triplets<0:l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    '''
                    Take example of [-3 -2 -2 0 0 2 2 3] and i=0
                    thus l,r lies between [-2 -2 0 0 2 2 3]
                    then when l=i+1 and all values of r, l=i+2 and all values of r, 
                    both set of solutions are equal
                    thus when nums[l]==nums[l-1] , we will increase l till l<r
                    '''
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res