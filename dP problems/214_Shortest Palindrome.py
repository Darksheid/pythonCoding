'''
214. Shortest Palindrome
You are given a string s. You can convert s to a
palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
'''

def shortestPalindrome(s):
        f,l=0,len(s)-1
        while f<=l:
            if f==l : break
            else:
                if s[f]==s[l] : f,l = f+1,l-1
                else:
                    s=s[:f]+s[l]+s[f:]
                    f =f+1
            print(f's = {s} , f={f} , l = {l}')
        return s

s="aabba"
print(shortestPalindrome(s))