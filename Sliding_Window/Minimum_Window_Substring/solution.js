// https://leetcode.com/problems/minimum-window-substring/
/**
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
*/

// Time O(N + M) | SpaceO(N + M)
const minWindow = (s, t) => {
  if (t == "") {
    return "";
  }

  let countT = new Map();
  let window = new Map();

  for (let i = 0; i < t.length; i++) {
    let value = 1;
    if (countT.has(t[i])) {
      value = countT.get(t[i]) + 1;
    }
    countT.set(t[i], value);
  }

  let have = 0;
  let need = countT.size;
  let res = [-1, -1];
  let resLen = Infinity;

  let l = 0;
  for (let r = 0; r < s.length; r++) {
    c = s[r];
    let value = 1;
    if (window.has(c)) {
      value = window.get(c) + 1;
    }
    window.set(c, value);

    if (countT.has(c) && window.get(c) === countT.get(c)) {
      have += 1;
    }

    while (have === need) {
      if (r - l + 1 < resLen) {
        res = [l, r];

        resLen = r - l + 1;
      }

      let popVal = window.get(s[l]) - 1;
      window.set(s[l], popVal);
      if (countT.has(s[l]) && window.get(s[l]) < countT.get(s[l])) {
        have -= 1;
      }
      l += 1;
    }
  }
  if (resLen != Infinity) {
    return s.slice(res[0], res[1] + 1);
  } else {
    return "";
  }
};

console.log(minWindow(s = "ADOBECODEBANC", t = "ABC"));
console.log(minWindow(s = "a", t = "aa"));
console.log(minWindow(s = "a", t = "a"));
