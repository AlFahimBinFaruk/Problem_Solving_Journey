// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Time O(log(N)) | Space O(1)
const findMin = (nums) => {
  let result = nums[0];

  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    let mid = Math.round(l + r);
    // if the array is sorted
    if (nums[l] < nums[r]) {
      result = Math.min(result, nums[l]);
      break;
    }

    result = Math.min(result, nums[mid]);
    if (nums[mid] >= nums[l]) {
      l = mid + 1;
    } else {
      r = mid - 1;
    }
  }

  return result;
};

console.log(findMin([4, 5, 6, 7, 0, 1, 2]));
console.log(findMin([3, 4, 5, 1, 2]));
