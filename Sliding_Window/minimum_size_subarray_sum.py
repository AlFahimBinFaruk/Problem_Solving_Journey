# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    # Time O(n) | Space O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0

        result = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(result,(r-l+1))
                total -= nums[l]
                l += 1
            r += 1    

        return result if result != float("inf") else 0 
