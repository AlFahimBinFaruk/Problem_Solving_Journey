// https://leetcode.com/problems/two-sum/
/**
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

 */

/**
 * Solution 01:
 * Hash Map - 1 Pass
 * Time O(N) | Space O(N)
 * @param {number[]} nums
 * @param {number} target
 * @returns
 */
const twoSumSolutionOne = (nums, target) => {
  prevMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    diff = target - nums[i];
    if (prevMap.has(diff)) {
      return [prevMap.get(diff), i];
    }
    prevMap.set(nums[i], i);
  }
  return false;
};

console.log(twoSumSolutionOne([2, 7, 11, 15], 9));
console.log(twoSumSolutionOne([2, 3, 3], 6));


/**
 * Solution 02: Hash Map - 2 Pass
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/two-sum/
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSumSolutionTwo = (nums, target) => {
    const map = getMap(nums);       /* Time O(N) | Space O(N) */

    return getSum(nums, target, map)/* Time O(N) */
}

const getMap = (nums, map = new Map()) => {
    for (let index = 0; index < nums.length; index++) {/* Time O(N) */
        map.set(nums[index], index);                        /* Space O(N) */
    }

    return map
}

const getSum = (nums, target, map) => {
    for (let index = 0; index < nums.length; index++) {/* Time O(N) */
        const complement = target - nums[index];
        const sumIndex = map.get(complement);

        const isTarget = map.has(complement) && (map.get(complement) !== index)
        if (isTarget) return [ index, sumIndex ]
    }

    return [ -1, -1 ];
}

console.log(twoSumSolutionTwo([2, 7, 11, 15], 9));
console.log(twoSumSolutionTwo([2, 3, 3], 6));

/**
 * Solution 03 : Brute Force - Linear Search
 * Time O(N^2) | Space O(1)
 * https://leetcode.com/problems/two-sum/
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSumSolutionThree = (nums, target) => {
  for (let curr = 0; curr < nums.length; curr++) {
    const diff = target - nums[curr];
    for (next = curr + 1; next < nums.length; next++) {
      let isTarget = diff === nums[next];
      if (isTarget) {
        return [curr, next];
      }
    }
  }
  return false;
};

console.log(twoSumSolutionThree([2, 7, 11, 15], 9));
console.log(twoSumSolutionThree([2, 3, 3], 6));
