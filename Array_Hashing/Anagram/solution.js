//  https://leetcode.com/problems/valid-anagram/

/***
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
***/

/**
 * Solution 01:Faster than 5.29% according to leetcode
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(N))
 * Time O(N * logN) | Space O(N)
 *
 * @param {string} s
 * @param {string} t
 * @returns {boolean}
 */
const isAnagramSolutionOne = (s, t) => {
  if (s.length != t.length) {
    return false;
  }

  return reorder(s) == reorder(t);
};

// This will sort the given string
const reorder = (str) => {
  return str
    .split("")
    .sort((a, b) => a.localeCompare(b))
    .join("");
};

console.log(isAnagramSolutionOne("cat", "rat"));
console.log(isAnagramSolutionOne("anagram", "nagaram"));

/**
 * Solution 02: Faster than 73.29% according to leetcode
 * Hash Map - Frequency Counter
 * Time O(N) | Space O(N)
 * @param {string} s
 * @param {string} t
 * @returns {boolean}
 */
const isAnagramSolutionTwo = (s, t, map = new Map()) => {
  if (s.length != t.length) {
    return false;
  }

  addFrequency(s, map);

  substractFrequency(t, map);

  return checkFrequency(map);
};

const addFrequency = (str, map) => {
  for (const char of str) {
    const count = (map.get(char) || 0) + 1;
    map.set(char, count);
  }
};

const substractFrequency = (str, map) => {
  for (const char of str) {
    if (!map.has(char)) {
      continue;
    }

    const count = map.get(char) - 1;
    map.set(char, count);
  }
};

const checkFrequency = (map) => {
  for ([char, count] of map) {
    const isEmpty = count == 0;

    if (!isEmpty) {
      return false;
    }
  }

  return true;
};

console.log(isAnagramSolutionTwo("cat", "rat"));
console.log(isAnagramSolutionTwo("anagram", "nagaram"));
