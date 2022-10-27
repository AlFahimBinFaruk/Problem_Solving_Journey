// https://leetcode.com/problems/longest-consecutive-sequence/
/**
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
*/

/**
 * Hash Set - Intelligent Sequence
 * Greedy - Max Score
 * Time O (N) | Space O(N)
 * @param {number[]} nums
 * @return {number}
 */
const longestConsequetiveSolutionOne = (nums) => {
  let numSet = new Set(nums);
  let longest = 0;

  for (let num of [...numSet]) {
    if (!numSet.has(num - 1)) {
      let length = 1;

      while (numSet.has(length + num)) {
        length += 1;
      }
      longest = Math.max(length, longest);
    }
  }

  return longest;
};

console.log(longestConsequetiveSolutionOne([100, 4, 200, 1, 3, 2]));
console.log(longestConsequetiveSolutionOne([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));

/**
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(K))
 * Greedy - Max Score
 * Time O (N * log(N)) | Space O(1)
 * @param {number[]} nums
 * @return {number}
 */
const longestConsequetiveSolutionTwo = (nums) => {
  nums.sort((a, b) => a - b);
  let length = 1;
  let longest = 1;

  for (let i = 1; i < nums.length; i++) {
    let isPrevDuplicate = nums[i - 1] === nums[i];
    if (isPrevDuplicate) continue;

    let isSteak = nums[i - 1] + 1 === nums[i];
    if (isSteak) {
      length += 1;
      continue;
    }
    longest = Math.max(length, longest);
    // reset length value for every iteration
    length = 1;
  }

  return Math.max(length, longest);
};

console.log(longestConsequetiveSolutionTwo([100, 4, 200, 1, 3, 2]));
console.log(longestConsequetiveSolutionTwo([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
console.log(
  longestConsequetiveSolutionTwo([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
);
