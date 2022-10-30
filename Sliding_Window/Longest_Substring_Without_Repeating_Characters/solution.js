// https://leetcode.com/problems/longest-substring-without-repeating-characters/
/**
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
*/

// Time O(N) | Space O(N)
const lenghtOfLongestSubstring = (s) => {
  let charSet = new Set();
  let length = 0;

  let l = 0;

  for (let r = 0; r < s.length; r++) {
    while (charSet.has(s[r])) {
      charSet.delete(s[l]);
      l += 1;
    }
    charSet.add(s[r]);
    length = Math.max(length, charSet.size);
  }

  return length;
};

console.log(lenghtOfLongestSubstring("abcabcbb"));
console.log(lenghtOfLongestSubstring("pwwkew"));
console.log(lenghtOfLongestSubstring("bbbbb"));
