// https://leetcode.com/problems/contains-duplicate/
/***
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

****/

/**
 * Solution 01:
 * Hash Set - Early Exit
 * Time O(N) | Space O(N)
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateSolutionOne = (nums) => {
  hashSet = new Set();

  for (const num of nums) {
    if (hashSet.has(num)) {
      return true;
    }
    hashSet.add(num);
  }
  return false;
};

console.log(containsDuplicateSolutionOne([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
console.log(containsDuplicateSolutionOne([1, 2, 3, 4]));

/**
 * Solution 02:
 * Hash Set
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateSolutionTwo = (nums) => {
  hashSet = new Set(nums);

  if (hashSet.size === nums.length) {
    return false;
  } else {
    return true;
  }
};

console.log(containsDuplicateSolutionTwo([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
console.log(containsDuplicateSolutionTwo([1, 2, 3, 4]));

/**
 * Solution 03:
 * Brute Force - Linear Search
 * Time O(N^2) | Space O(1)
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateSolutionThree = (nums) => {
  for (let right = 0; right < nums.length; right++) {
    for (let left = 0; left < right; left++) {
      const isDuplicate = nums[left] === nums[right];
      if (isDuplicate) {
        return true;
      }
    }
  }
  return false;
};

console.log(containsDuplicateSolutionThree([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
console.log(containsDuplicateSolutionThree([1, 2, 3, 4]));

/**
 * Solution 04:
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(N))
 * Time O(N * log(N)) | Space O(1)
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateSolutionFour = (nums) => {
  // this will sort the array
  nums.sort((a, b) => a - b);

  return hasDuplicate(nums)
};

const hasDuplicate = (nums) => {
  for (let current = 0; current < nums.length - 1; current++) {
    const next = current + 1;

    const isDuplicate = nums[current] == nums[next];

    if (isDuplicate) {
      return true;
    }
  }
  return false;
};

console.log(containsDuplicateSolutionFour([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
console.log(containsDuplicateSolutionFour([1, 2, 3, 4]));
