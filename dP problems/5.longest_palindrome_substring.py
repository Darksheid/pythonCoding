'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''



def longestPalindrome(s):
        n = len(s)
        maxlen = 0
        substr = ""
        dp = [[False] * n for _ in range(n)]
        '''
        # this dp table will hold true/False value if s[i..j] is Palindrome

        # base case when single char is there in the String s[i..i]=s[i]
        '''
        for k in range(n):
            dp[k][k] = True

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                '''
                # eliminate cases when i>j
                # case when i==j is already calculated to be True
                '''
                if j > i:
                    '''
                    # Case when two string is present, palindrome if both the strings are equal
                    '''
                    if j - i == 1 and s[i] == s[j]:
                        dp[i][j] = True
                    elif j - i > 1:
                        '''
                        say for case i=1,j=4 => 'abad', it will be palindrome when 
                            1>  'a' == 'd'  (s[i]==s[j]) and 
                            2>  'ba' is palindrome (dp[i+1][j-1] is true)
                        '''
                        dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                # Take the max of length if the subsequence is True
                if dp[i][j] and j - i + 1 > maxlen:
                    substr = s[i:j + 1]
                    maxlen = j - i + 1

        return substr

s='babad'
print(longestPalindrome(s))