'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

############################################Solution######################################
BRUTE FORCE TimeComplexity O(n^2); Space complexity O(1):
To be observed that in the for pos i and j such that j>=i, if jth element count in s[i:j] is more than 1
then the case will not be considered in the solution set, and sebsequntly j+1th element count in s[i:j+1]
will also have duplicates,so we can ignore those values,
Thus get all positions of i and j and check that jth element count in the s[i:j] is more than 1
if not then compare with previous max values and take the max, if true then break from the loop
return maxcount

Optimized TimeComplexity O(n); Space complexity O(n):
We keep a track for left,right pointers, and traverse the string ,
as we traverse the string we keep incrementing the right pointer and keep the traversed elements in a list/set
if we find such element which is already present in the list/set,then we start removing the element starting from left position
till there is no such elements in the set which is equal to right position element, incrementing the left position value,
now we know the resultant l,r is the pointers between which there are no duplicates
take max of previous l,r to current l,r
return the maxcount
'''

#BRUTE FORCE
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    maxcount = 0
    for i in range(n):
        for j in range(i, n):
            #print(f"{s[j]} in {s[i:j+1]} is {s[j] in s[i:j + 1]} ")
            if s[i:j + 1].count(s[j]) > 1:
                break
            else:
                maxcount = max(maxcount, j - i + 1)

    return maxcount

#BRUTE FORCE
def lengthOfLongestSubstring2(s: str) -> int:
    n = len(s)
    l, r = 0, 0
    maxcount = 0
    while r < n:
        print(f"Count of {s[r]} in {s[l:r+1]} is {s[l:r + 1].count(s[r])} ")
        if s[l:r + 1].count(s[r]) > 1:
            l += 1
            r = l
        else:
            maxcount = max(maxcount, r - l + 1)
        r += 1
    return maxcount

#Optimized
def lengthOfLongestSubstringOptimized(self, s: str) -> int:
        n = len(s)
        l=0
        myset = list()
        maxcount = 0
        for r in range(n):
            while s[r] in myset:
                myset.remove(s[l])
                l+=1
            myset.append(s[r])
            maxcount = max(maxcount, r - l + 1)

        return maxcount


s = "pwwkew"
#print(s.count('a'))
print(lengthOfLongestSubstringOptimized(s))
