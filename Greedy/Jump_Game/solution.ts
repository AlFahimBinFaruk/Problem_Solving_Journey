// Time O(N) | Space O(1)
function canJump(nums: number[]): boolean {
  let goal: number = nums.length - 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    if (nums[i] + i >= goal) {
      goal = i;
    }
  }

  if (goal == 0) {
    return true;
  }

  return false;
}
