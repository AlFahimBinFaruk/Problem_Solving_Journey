# https://leetcode.com/problems/group-anagrams/
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

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
strs[i] consists of lowercase English letters.
"""

"""
Solution:Hash-map
time-complexity: O(M*N)
"""

import collections


# Solution : hash-map : Time O(N * M) | Space O(N * M)

def groupAnagram(strs):
    # defining a dictionary with default values as an empty list / [].which means if a key dosent exits it will not raise keyError rather it will return and empty list : []
    result = collections.defaultdict(list)

    for str in strs:
        count = [0]*26
        for char in str:
            count[ord(char)-ord("a")] += 1
        result[tuple(count)].append(str)
    return result.values()


print(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
