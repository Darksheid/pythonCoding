'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
 all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

def isPalindrome(s):
    s = s.lower()
    modified_s = ""
    for ch in s:
        if (ord(ch) >= ord("a") and ord(ch) <= ord("z")) or (ord(ch) >= ord("0") and ord(ch) <= ord("9")):
            modified_s += ch
    if modified_s[::-1] == modified_s: return True
    return False
s="Was it a car or a cat I saw?"
print(isPalindrome(s))