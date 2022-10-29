# https://leetcode.com/problems/valid-palindrome/
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

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
"""

# Solution 01 : With build in Methods
# Time O(N) | Space O(N)
def isPalindromeSolutionOne(s):
    if not len(s):
        return False
    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()

    return newStr == newStr[::-1]


print(isPalindromeSolutionOne("A man, a plan, a canal: Panama"))
print(isPalindromeSolutionOne("race a car"))


# Solution 02 : with Custom method
# Time O(N) | Space O(1)
def isPalindromeSolutionTwo(s):
    if not len(s):
        return False
    l = 0
    r = len(s)-1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1
    return True


def alphaNum(s):
    return (ord("A") <= ord(s) <= ord("Z") or ord("a") <= ord(s) <= ord("z") or ord("0") <= ord(s) <= ord("9"))


print(isPalindromeSolutionTwo("A man, a plan, a canal: Panama"))
print(isPalindromeSolutionTwo("race a car"))
