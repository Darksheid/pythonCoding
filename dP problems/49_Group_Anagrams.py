'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase E
'''
from collections import defaultdict
def groupAnagrams(strs):
        ans = defaultdict(list)
        #To not to return any error key
        for s in strs:
            #maps 0-> a,1-b,2->c and so on....25->z
            count = [0] * 26
            for c in s:
                #ord(c) will provide the ascii value
                count[ord(c) - ord("a")] += 1
            #list is not hashable but tuples are hashable,thus tuple is used to get the key values from dict
            #for each count, we will apend the list
            '''
            ans[tuple(count)] will return the list (amend is done on the list) with tuple(count) as key
            if no such key is found then error is not thrown as its a defaultdict
            '''
            ans[tuple(count)].append(s)

        return ans.values()
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
