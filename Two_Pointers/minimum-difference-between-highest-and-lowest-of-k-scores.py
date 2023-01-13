# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
class Solution:
    # Time O(N)
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1 # to make sure the window size is k.
        result = float("inf")
        while r < len(nums):
            result = min(result,(nums[r]-nums[l]))
            l += 1
            r += 1
        return result    
