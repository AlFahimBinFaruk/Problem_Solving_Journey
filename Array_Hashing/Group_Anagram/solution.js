// https://leetcode.com/problems/group-anagrams/
/**
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
 */

/**
 * Solution 01: Hash Map
 * Time O(N * M) | Space O(N * M)
 * @param {string[]} words
 * @return {string[][]}
 */
const groupAnagramSolutionOne = (strs) => {
  result = new Map();

  for (let str of strs) {
    let count = new Array(26).fill(0);

    for (let char of str) {
      count[char.charCodeAt(0) - "a".charCodeAt(0)] += 1;
    }
    count = generateHash(count);

    const values = result.get(count) || [];
    values.push(str);
    result.set(count, values);
  }

  return [...result.values()];
};

const generateHash = (val) => {
  return val.map((count) => `#${count}`).join("");
};

console.log(
  groupAnagramSolutionOne(["eat", "tea", "tan", "ate", "nat", "bat"])
);

/**
 * Solution 02: Sort - HeapSort Space O(1) | QuickSort Space O(log(K))
 * Hash Map - Adjacency List
 * Time O(N * (M * log(M))) | Space O(N * M)
 * https://leetcode.com/problems/group-anagrams/
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagramSolutionTwo = (strs) => {
  result = new Map();

  for (let str of strs) {
    const sorted = reorder(str);
    const values = result.get(sorted) || [];
    values.push(str);
    result.set(sorted, values);
  }
  return [...result.values()];
};

const reorder = (str) => {
  return str
    .split("")
    .sort((a, b) => a.localeCompare(b))
    .join("");
};

console.log(
  groupAnagramSolutionTwo(["eat", "tea", "tan", "ate", "nat", "bat"])
);
