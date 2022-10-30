// https://leetcode.com/problems/longest-repeating-character-replacement/
/**
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
*/

// Time O(N) | Space O(N)
const characterReplacement = (s, k) => {
  let charSet = new Map();
  let maxFreq = 0;
  let maxLength = 0;

  let l = 0;
  for (let r = 0; r < s.length; r++) {
    let value = 1;
    if (charSet.has(s[r])) {
      value = charSet.get(s[r]) + 1;
    }
    charSet.set(s[r], value);

    maxFreq = Math.max(maxFreq, charSet.get(s[r]));
    if (r - l + 1 - maxFreq > k) {
      let value = charSet.get(s[l]) - 1;
      charSet.set(s[l], value);
      l += 1;
    }

    maxLength = Math.max(maxLength, r - l + 1);
  }
  return maxLength;
};

console.log(characterReplacement("AABABBA", 1));
console.log(characterReplacement("ABAB", 2));
