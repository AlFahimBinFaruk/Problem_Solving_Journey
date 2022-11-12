// Time O(N) | Space O(1)
function maxSubArray(nums: number[]): number {
  let res: number = nums[0];

  let total: number = 0;

  for (let i = 0; i < nums.length; i++) {
    let n: number = nums[i];
    total += n;
    res = Math.max(res, total);
    if (total < 0) {
      total = 0;
    }
  }

  return res;
}
