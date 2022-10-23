# https://leetcode.com/problems/valid-anagram/

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.(একটি অ্যানাগ্রাম হল একটি শব্দ বা বাক্যাংশ যা একটি ভিন্ন শব্দ বা বাক্যাংশের অক্ষরগুলিকে পুনর্বিন্যাস করে গঠিত হয়, সাধারণত সমস্ত মূল অক্ষরগুলিকে একবার ব্যবহার করে।)

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def isAnagram(s, t) -> bool:
    # Solution 01
    # return sorted(s) == sorted(t)

    # Solution 02
    # return Counter(s) == Counter(t)

    # Solution 03 : hashmap
    if len(s) != len(t):
        return False

    counterS = {}
    counterT = {}

    for i in range(len(s)):
        counterS[s[i]] = counterS.get(s[i], 0) + 1
        counterT[t[i]] = counterT.get(t[i], 0) + 1

    # return counterS == counterT

    for t in counterT:
        if counterT[t] != counterS.get(t,0):
            return False
    
    return True


print(isAnagram("cat", "rat"))
print(isAnagram("anagram", "nagaram"))
