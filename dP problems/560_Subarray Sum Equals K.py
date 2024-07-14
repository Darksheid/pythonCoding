'''
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

#####################################################Solution########################################################
If we check the constraints , then we will be able to find that Sliding window doesn't work , reason : if the
contiguous sum is greater/lesser than Target sum, if we slide the left and right pointers then the resultant sum may
not increase/decrease as there are negative numbers

Brute Force [Time Complexity O(n2)] :
take every possible contiguous arrays and check the condition

Optimal Solution [Time Complexity O(n) Space Complexity O(n) ]
We take a loop and get the sum for say ith index of the loop, currSum variable
Now we calculate the difference from Target Sum to currSum , diff = currSum - k
diff variable shows that diff sum is required so that total subarray sum becomes k till ith index
So that array could be counted as solution set,
thus we have to check if we are getting currSum == diff at some point while travering till i
We Store the value of currSum in a HashMap, key : currSum ; Value : Counts of Same currSum
While traversing if we get same currSum we increment the value by 1
and simultaneously we check if diff value is present in the HashMap, if yes then
res_count is updated by the count of diff map.get(diff)

'''
#Optimized
def subarraySum(nums,k):
    currSum = 0
    res= 0
    prefixMap= {0:1} # it means that subarray prior to 0th index sum =0(nothing is selected)

    for num in nums:
        currSum += num
        diff = currSum - k
        res += prefixMap.get(diff,0)
        # if diff is not present then 0 is returned and add the value to existing res value
        # #it also emulated that fact that until ith index if we are getting diff or not
        # Finally updates the map with the currSum,if currSum is found in the map by 1
        prefixMap[currSum] = 1+ prefixMap.get(currSum,0)
    return res

