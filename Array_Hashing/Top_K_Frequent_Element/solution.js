// https://leetcode.com/problems/top-k-frequent-elements/
/**
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */

/**
 * Hash Map - Frequency Counter
 * Matrix - Bucket
 * Time O(N^2) | Space O(N^2)
 * https://leetcode.com/problems/top-k-frequent-elements/
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequentSolutionOne = (nums, k) => {
  let count = new Map();
  let freq = new Array(nums.length + 1).fill().map(() => []);

  for (let num of nums) {
    let value = (count.get(num) || 0) + 1;
    count.set(num, value);
  }

  for (let [key, val] of count.entries()) {
    freq[val].push(key);
  }

  freq.reverse();

  result = [];
  for (let i of freq) {
    for (let j of i) {
      result.push(j);
      if (result.length === k) {
        return result;
      }
    }
  }
};
console.log(topKFrequentSolutionOne([1, 1, 1, 2, 2, 3], 2));
console.log(topKFrequentSolutionOne([3, 0, 1, 0], 1));
