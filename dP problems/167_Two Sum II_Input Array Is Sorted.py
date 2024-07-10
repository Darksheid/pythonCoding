'''
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your soltion must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

Solution(Optimal O(n) time)
lets take arr = [1,3,4,5,7,10,11] (already sorted in increasing order as in question)
and target = 9
if we take two pointer first , last  = 0 , n-1 index of array
1>>now arr[first] + arr[last] =12> Target , in such case we cannot increase first, this will only increase the sum
    thus last pointer to be decreased by 1
2>>now arr[first] + arr[last] =11 > Target, last =last-1
3>>arr[first] + arr[last] =8< target , in this case we have increase the sum, hence first = first +1
4>>arr[first] + arr[last] =10> target , last-=1
5>>arr[first] + arr[last] =8<target ,first+=1
6>>arr[first] + arr[last] =9 , return [first+1,Last+1]
'''


def twoSum(numbers, target):
    n = len(numbers)
    f, l = 0, n - 1
    n = len(numbers)
    while True:
        if numbers[f] + numbers[l] == target:
            return [f + 1, l + 1]
        elif numbers[f] + numbers[l] < target:
            f += 1
        else:
            l = l - 1


numbers = [1,3,4,5,7,10,11]
target = 9
print(twoSum(numbers, target))
num=[-1,0,1,2,-1,4]

print(sorted(num))
